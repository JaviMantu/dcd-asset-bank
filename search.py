#!/usr/bin/env python3
"""Search the dcd asset bank from its root (Python 3.9, stdlib only; no network, no embeddings).

  python3 search.py "<query>" [--family scenes] [--vertical banca] [--intent hero] [--k 10] [--json]
  python3 search.py --related <id> [--k 10] [--json]
  python3 search.py selftest

BM25 (k1 1.5, b 0.75) over each card: the intent's Spanish words ×4 (`keywords`, from vocab.json), title ×3, tags ×2
(vertical label, aliases and words included), description and the card body ×1; then the score is multiplied by
1 + 0.5 per query word that is one of the record's intent words (an exact «antes»/«después» beats a body mention). Accents and case are folded
(«energía» = «energia»). --family / --vertical / --intent keep only the records whose field holds that exact value.
--related <id> lists the graph neighbours of a record (graphify-out/graph.json) with their relation, after the ranked
`related` of the record (the same graph built them). Reads index.jsonl and cards/ next to this file.
"""
from __future__ import annotations

import json
import math
import re
import sys
import tempfile
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STOP = set("a al con de del el en es la las lo los o para por que se su sus un una uno y the of and to in for is on "
           "with as by it an or at from this that".split())
WEIGHTS = (("keywords", 4), ("title", 3), ("title_en", 3), ("tags", 2), ("description", 1), ("description_en", 1), ("body", 1))


def fold(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", str(text).lower()) if unicodedata.category(c) != "Mn")


def tokens(text: str) -> list:
    return [t for t in re.findall(r"[a-z0-9]+", fold(text)) if t not in STOP and len(t) > 1]


def load(root: Path = ROOT) -> list:
    recs = [json.loads(line) for line in (root / "index.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    for r in recs:
        card = root / r["card"]
        text = card.read_text(encoding="utf-8") if card.is_file() else ""
        r["body"] = text.split("\n---\n", 1)[-1]
    return recs


def bm25(recs: list, query: str, k1: float = 1.5, b: float = 0.75) -> list:
    docs = []
    for r in recs:
        tf: dict = {}
        for field, w in WEIGHTS:
            val = r.get(field, "")
            for t in tokens(" ".join(val) if isinstance(val, list) else val):
                tf[t] = tf.get(t, 0) + w
        docs.append(tf)
    n = len(docs) or 1
    avg = sum(sum(d.values()) for d in docs) / n or 1
    q = tokens(query)
    df = {t: sum(1 for d in docs if t in d) for t in set(q)}
    out, qs = [], set(q)
    for r, d in zip(recs, docs):
        ln, s = sum(d.values()), 0.0
        for t in q:
            if t in d:
                idf = math.log(1 + (n - df[t] + 0.5) / (df[t] + 0.5))
                s += idf * d[t] * (k1 + 1) / (d[t] + k1 * (1 - b + b * ln / avg))
        hit = len(qs & set(tokens(" ".join(r.get("keywords", [])))))
        s *= 1 + 0.5 * hit                                                # exact intent-word hits: ×1.5 each
        if s > 0:
            out.append((round(s, 4), r["id"], r))
    return sorted(out, key=lambda x: (-x[0], x[1]))


def search(recs: list, query: str, family: str = "", vertical: str = "", intent: str = "", k: int = 10) -> list:
    keep = [r for r in recs if (not family or r["family"] == family) and (not vertical or vertical in r["vertical"])
            and (not intent or intent in r["intent"])]
    return bm25(keep, query)[:k]


def related(root: Path, rid: str, k: int = 10) -> dict:
    recs = {r["id"]: r for r in load(root)}
    g = json.loads((root / "graphify-out" / "graph.json").read_text(encoding="utf-8"))
    if rid not in {n["id"] for n in g["nodes"]}:
        raise SystemExit(f"search: no node «{rid}» in graphify-out/graph.json")
    label = {n["id"]: n["label"] for n in g["nodes"]}
    edges = sorted({(e["relation"], "->" if e["source"] == rid else "<-", e["target"] if e["source"] == rid else e["source"])
                    for e in g["links"] if rid in (e["source"], e["target"])})
    ranked = recs.get(rid, {}).get("related", [])[:k]
    return {"id": rid, "related": [{"id": x, "title": recs[x]["title"], "card": recs[x]["card"]} for x in ranked if x in recs],
            "edges": [{"relation": r, "dir": d, "id": x, "label": label.get(x, x)} for r, d, x in edges]}


def selftest() -> None:
    assert fold("Energía ÁRBOL") == "energia arbol" and tokens("la energía de su operación") == ["energia", "operacion"]
    with tempfile.TemporaryDirectory() as t:
        root = Path(t)
        (root / "cards").mkdir()
        rows = [("a", "scenes", "Turbina de energía", ["energia"], ["hero"], "una turbina gira"),
                ("b", "scenes", "Crédito rápido", ["banca"], ["gap"], "la energía del crédito"),
                ("c", "arcs", "Arco banca", ["banca"], ["hero"], "banca y crédito")]
        with open(root / "index.jsonl", "w", encoding="utf-8") as f:
            for rid, fam, title, vert, intent, body in rows:
                (root / "cards" / f"{rid}.md").write_text(f"---\nid: \"{rid}\"\n---\n{body}\n", encoding="utf-8")
                f.write(json.dumps({"id": rid, "family": fam, "title": title, "title_en": "", "tags": vert + intent,
                                    "description": "", "description_en": "", "vertical": vert, "intent": intent,
                                    "related": [x for x in "abc" if x != rid], "card": f"cards/{rid}.md"}) + "\n")
        (root / "graphify-out").mkdir()
        (root / "graphify-out" / "graph.json").write_text(json.dumps({"nodes": [{"id": x, "label": x} for x in "abc"], "links": [
            {"source": "a", "target": "b", "relation": "pairs_with"}, {"source": "c", "target": "a", "relation": "uses_scene"}]}))
        recs = load(root)
        top = search(recs, "ENERGIA")
        assert [x[1] for x in top] == ["a", "b"], top                     # title ×3 beats a body mention
        assert [x[1] for x in search(recs, "credito", vertical="banca", family="arcs")] == ["c"]
        assert search(recs, "hero", intent="gap") == []
        rel = related(root, "a")
        assert [e["id"] for e in rel["edges"]] == ["b", "c"] and rel["edges"][1]["dir"] == "<-", rel
    if (ROOT / "index.jsonl").is_file():                                  # inside a bank: the real index answers
        recs = load()
        assert search(recs, "portada", family="scenes"), "no scene answers «portada»"
    print("search selftest: OK")


def main(argv: list) -> int:
    if argv[:1] == ["selftest"]:
        selftest()
        return 0
    opt = lambda name, dflt="": argv[argv.index(name) + 1] if name in argv else dflt
    k = int(opt("--k", "10"))
    if "--related" in argv:
        res = related(ROOT, opt("--related"), k)
        if "--json" in argv:
            print(json.dumps(res, ensure_ascii=False, indent=1))
        else:
            print(f"# {res['id']}")
            for r in res["related"]:
                print(f"related  {r['id']:32} {r['title']}  ({r['card']})")
            for e in res["edges"]:
                print(f"{e['relation']:12} {e['dir']} {e['id']}")
        return 0
    flags = {"--family", "--vertical", "--intent", "--k"}
    words = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] not in flags)]
    if not words:
        print(__doc__)
        return 2
    hits = search(load(), " ".join(words), opt("--family"), opt("--vertical"), opt("--intent"), k)
    if "--json" in argv:
        print(json.dumps([{"score": s, "id": i, "family": r["family"], "title": r["title"], "card": r["card"]}
                          for s, i, r in hits], ensure_ascii=False, indent=1))
    else:
        for s, i, r in hits:
            print(f"{s:8.3f}  {r['family']:10} {i:32} {r['title']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
