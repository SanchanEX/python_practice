import sys
from pprint import pprint


def read_file(file_path):
    titles, types = [], []
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, tit, typ, *_ = row.rstrip().split("\t")
            titles.append(tit)
            types.append(set(typ.split()))
    return titles, types    # 全ポケモン, そのタイプ


class Team(dict):
    def __setitem__(self, tit, types):
        if types in self.values():
            raise ValueError("このタイプのポケモンはすでにチームに存在します．")
        if tit in self.keys():
            raise ValueError("このタイプのポケモンはすでにチームに存在します．")
        super().__setitem__(tit, types)


if __name__ == "__main__":
    titles, types = read_file(sys.argv[1])
    team = Team()
    for title, type_set in zip(titles, types):
        try:
            team[title] = type_set  # __setitem__発火
            # print(team[title])
        except Exception as e:
            print(e)

    print(len(team))
    pprint(team)
