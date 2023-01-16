from pprint import pprint
from collections import Counter


def read_types(file_path):
    types = list()
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, _, typ, *_ = row.rstrip().split("\t")
            types.append(frozenset(typ.split()))

    return types  # タイプ文字列のfrozensetが並ぶリスト


if __name__ == "__main__":
    types = read_types("../data/poke_names.txt")
    typ_cnt = Counter(types)
    # pprint(typ_cnt.most_common(5))
    pprint(typ_cnt)
