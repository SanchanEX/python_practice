import sys


def read_names(file_path):
    titles = []
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, tit, _, *_ = row.rstrip().split("\t")
            titles.append(tit)
    return titles


def name_generator(lst, char):
    pass


if __name__ == "__main__":
    titles = read_names(sys.argv[1]) # lec04/data/poke_names.txt
    char = sys.argv[2] # リー
