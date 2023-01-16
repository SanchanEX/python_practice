import sys
from pprint import pprint
from dataclasses import dataclass


@dataclass
class Monster:
    title: str


class Zukan(list):
    def append(self, value):
        if not isinstance(value, Monster):
            raise ValueError("Monsterクラス以外のインスタンスは登録できません．")
        super().append(value)


def read_names(file_path):
    titles = list()
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, tit, _, *_ = row.rstrip().split("\t")
            titles.append(tit)
    return titles


if __name__ == "__main__":
    titles = read_names(sys.argv[1])
    zukan = Zukan()
    for title in titles:
        zukan.append(Monster(title))
    pprint(zukan)
    try:
        zukan.append(251)
        print(zukan)
    except Exception as e:
        print(e)
