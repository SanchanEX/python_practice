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
    # pattern = re.compile("(ュウ|ュー)$")
    # pattern = re.compile("ン.*ン")  # ンを2回含む
    # pattern = re.compile("[ラリルレロ].*[ラリルレロ].*")  # ラリルレロのいずれかを2回以上含む
    # pattern = re.compile("^.{3}$")   # 3文字の名前
    pattern = re.compile("ッ(.{1}|.{2})$")    # ッと任意の1文字 or 2文字で終わる名前
    for i, title in enumerate(titles, 1):
        match = pattern.search(title)
        if match:   # matchした場合のみ表示
            print(title, match)
