class Monster:
    def __init__(self, tit):
        self.tit = tit

    def __eq__(self, other):
        return self.tit == other.tit


class ZukanMonster(Monster):
    def __init__(self, tit, spe, typ):
        super().__init__(tit)   # 名前を継承
        self.spe = spe      # 分類を設定
        self.typ = typ      # タイプを設定

    def __str__(self):
        return f"なまえ：{self.tit}\nぶんるい：{self.spe}\n{self.typ}"


class Zukan():
    def __init__(self, f):
        self.f_l = Zukan.read_names(f)

    def read_names(file_path):
        names = []
        with open(file_path, "r", encoding="utf8") as rfo:
            for row in rfo:
                _, tit, spe, typ = row.rstrip().split("\t")
                names.append(ZukanMonster(tit, spe, typ))
        return names

    def search_monster(self, tg):
        for monster in self.f_l:
            if monster == tg:
                return monster
            else:
                pass
        return f"{tg.tit}は図鑑に登録されていない新種です．"
