class Monster:
    def __init__(self, name, s):
        self.tit, self.spe, self.typ = name
        self.s = s
        self.__level = 0

    def __str__(self):
        return f"{self.tit}(Lv.{self.level})"

    def __gt__(self, other):
        return sum(self.s) + self.level > sum(other.s) + other.level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, val):
        if val < 0:
            print("不正な値のため，符号を反転して設定します．")
            val *= -1
        self.__level = val


def read_names(file_path):
    names = []
    with open(file_path, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, tit, spe, typ = row.rstrip().split("\t")
            names.append([tit, spe, typ])
    return names


def read_stats(file_path):
    stats = []
    with open(file_path, "r") as rfo:
        for row in rfo:
            row = row.rstrip()
            stats.append([int(col) for col in row.split(" ")])
    return stats
