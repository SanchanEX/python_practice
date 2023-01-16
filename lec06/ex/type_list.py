from pprint import pprint
from collections import defaultdict


def read_types(file_path):
    types = dict()
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, tit, typ, *_ = row.rstrip().split("\t")
            types[tit] = typ.split()
    return types


if __name__ == "__main__":
    types = read_types("../data/poke_names.txt")
    typ_lst = defaultdict(list)  # 空のlistをデフォルト値
    for title, types in types.items():
        # print("="*30)
        # print(title, types)
        for type_ in types:
            # print("="*30)
            # print(typ_lst)
            # print(type_)
            typ_lst[type_].append(title)
    # pprint(typ_lst)
