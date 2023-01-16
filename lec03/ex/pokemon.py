from random import choice, randint


def read_files(file_path1, file_path2):
    def read_stats(file_path):
        """ 統計infoを操作する関数 """
        stats = []  # statsを初期化して定義
        with open(file_path, "r") as rfo:
            for row in rfo:
                row = row.rstrip()  # 末尾削除
                stats.append([      # 追加 *
                    int(col)        # 整数化する ↑
                    for col in row.split(" ")   # 空白を基準にリスト化し，1つずつ取得　↑
                ])
        return stats    # 5つの能力を1つのリストとされている

    def read_names(file_path):
        """ ポケモンの名前を操作する関数 """
        names, types, evols = [], [], []    # names, types, evolsを初期化して定義
        with open(encoding="utf8", file=file_path, mode="r") as rfo:    # file_pathに指定したファイルを開く
            for row in rfo:   # 1行ずつ取り出し，回す
                _, nam, typ, *evo = row.rstrip().split("\t")    # タブで区切る, rstripで末尾削除
                names.append(nam)              # 名前をappend
                types.append(typ.split(" "))   # タイプをappend, -> 空白を基準にリストにする
                # 進化先のリストをappend -> evoのままでもOKなのでは？
                evols.append([e for e in evo])
                # print(row.rstrip().split("\t"))
                # print(typ.split(" "))
                # print('=========================')
                # print([e for e in evo])
                # print(evo)
                # print('=========================')

        return names, types, evols  # セットしたものをreturnする

    stats = read_stats(file_path1)  # 第一引数に統計データ
    names, types, evols = read_names(file_path2)    # 第二引数にポケモン
    return stats, names, types, evols   # 4つのリストのタプル


class Monster:
    def __init__(self, title):
        self.title = title
        self.type_ = None
        self.evols = None
        self.attacks = []
        self.defenses = []
        self.level = randint(5, 100)
        self.stats = []

    def set_types(self, t1, t2=None):
        self.type1 = t1
        self.type_ = t1
        if t2:
            self.type2 = t2
            self.type_ += " " + t2

    def set_evols(self, *args):
        self.evols = args   # 進化系を引数から取得し，代入

    def evolve(self):
        """ 進化を操作する関数 """
        if self.evols:      # 進化系が存在するなら
            evo_name = choice(self.evols)   # 進化系の名前
            print(f"{evo_name}にevolve")    # print
            return evo_name
        else:
            print("evolveできません")
            return None

    def attack(self):
        """ 攻撃を操作する関数 """
        if self.attacks:    # 攻撃があるなら
            atk_name = choice(self.attacks)
            print(f"{atk_name}でattack")
            return atk_name
        else:
            print("attackできません")
            return None

    def defense(self):
        """ 防御を操作する関数 """
        if self.defenses:   # 防御があるなら
            def_name = choice(self.defenses)
            print(f"{def_name}でdefense")
            return def_name
        else:
            print(f"defenseできません")
            return None

    def __gt__(self, other):
        return self.level > other.level

    def __lt__(self, other):
        return self.level < other.level

    def __eq__(self, other):
        return self.title == other.title

    def __repr__(self):
        return self.title
