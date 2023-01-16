from pprint import pprint
from collections import Counter


def read_types(file_path):
    types = list()
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, _, typ, *_ = row.rstrip().split("\t")
            ts = typ.split(" ")
            if len(ts) != 2:
                continue
            (t1, t2) = (ts[0], ts[1]) if ts[0] < ts[1] else (ts[1], ts[0])
            types.append(frozenset({t1, t2}))

    return types  # タイプ文字列のfrozensetが並ぶリスト


if __name__ == "__main__":
    types = read_types("../data/poke_names.txt")
    typ_cnt = Counter(types)
    # res = sorted(typ_cnt.items(), key=lambda tp: tp[1], reverse=True)
    pprint(typ_cnt)
