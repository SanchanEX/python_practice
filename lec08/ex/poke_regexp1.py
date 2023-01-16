import re


def read_names(file_path):
    titles = list()
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, tit, _, *_ = row.rstrip().split("\t")
            titles.append(tit)
    return titles


if __name__ == "__main__":
    titles = read_names("../data/poke_names.txt")
    pattern = re.compile("ー")  # 長音　パターンクラスのインスタンス
    print(pattern, type(pattern))
    for i, title in enumerate(titles, 1):
        print(title, pattern.findall(title))
        if i == 20:
            break
