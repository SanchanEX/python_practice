from random import randint
from time import process_time


def read_names(file_path):
    titles = list()
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, tit, _, *_ = row.rstrip().split("\t")
            titles.append(tit)
    return titles


class Monster:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title

    def __eq__(self, other: "Monster"):
        return self.title == other.title

    # def __hash__(self):
    #     """
    #     不適切なハッシュ値を返す
    #     等価なオブジェクトでも異なるハッシュ値となる可能性がある
    #     """
    #     return randint(1, 100000000000000)

    # def __hash__(self):
    #     """
    #     不適切なハッシュ値を返す
    #     等価でないオブジェクトでも同じハッシュ値となる
    #     """
    #     return 1

    def __hash__(self):
        """
        適切なハッシュ値を返す
        等価なオブジェクトは同じハッシュ値となる
        """
        return hash(self.title)


if __name__ == "__main__":
    pika1 = Monster("ピカチュウ")
    pika2 = Monster("ピカチュウ")
    fushi = Monster("フシギダネ")
    print(pika1 == pika2)   # 等価
    print(hash(pika1) == hash(pika2))  # hashも等価
    print(pika1 == fushi)   # 不等価
    print(hash(pika1) == hash(fushi))  # hashも不等価

    mon_set = set([pika1, pika2, fushi])  # 一応ハッシュ値を返す__hash__を持つので，集合の要素となれる
    print(mon_set)
    print("#"*20)

    titles = read_names("../../lec06/data/poke_names.txt")
    mons = set([Monster(title) for title in titles])

    begin = process_time()
    for _ in range(999):
        mons |= set([Monster(title) for title in titles])
    end = process_time()

    print(f"所要時間：{end-begin}")    # かかった時間をprint
    print(len(mons))
