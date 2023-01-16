from pprint import pprint
from collections import defaultdict


def read_names(file_path):
    titles = list()
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, tit, _, *_ = row.rstrip().split("\t")
            titles.append(tit)
    return titles


if __name__ == "__main__":
    titles = read_names("../data/poke_names.txt")
    chr_counts = defaultdict(int)

    for title in titles:
        for t in title:
            chr_counts[t] += 1

    pprint(chr_counts)  # 文字がキー，出現数が値
