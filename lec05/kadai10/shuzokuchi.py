class ShuzokuchiDesc:
    def __set_name__(self, owner, attrname):
        self.attrname = attrname

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.attrname]

    def __set__(self, obj, value):
        if (1 <= value <= 255):
            obj.__dict__[self.attrname] = value
        else:
            raise ValueError("種族値規定違反")


class Shuzokuchi:
    hp = ShuzokuchiDesc()
    kou = ShuzokuchiDesc()
    bou = ShuzokuchiDesc()
    tkou = ShuzokuchiDesc()
    tbou = ShuzokuchiDesc()
    suba = ShuzokuchiDesc()

    def __init__(self, hp, kou, bou, tkou, tbou, suba):
        self.hp = hp
        self.kou = kou
        self.bou = bou
        self.tkou = tkou
        self.tbou = tbou
        self.suba = suba
        self.sumstatus = self.hp + self.kou + \
            self.bou + self.tkou + self.tbou + self.suba

    def __repr__(self) -> str:
        return f"H:{self.hp} A:{self.kou} B:{self.bou} C:{self.tkou} D:{self.tbou} S:{self.suba} 合計:{self.sumstatus}"

    # 参照可能
    def __getitem__(self, item):
        if item == "hp":
            return self.hp
        if item == "kou":
            return self.kou
        if item == "bou":
            return self.bou
        if item == "tkou":
            return self.tkou
        if item == "tbou":
            return self.tbou
        if item == "suba":
            return self.suba
        if item == "合計":
            return self.sumstatus

    # 加算
    def __add__(self, other):
        hp = self.hp + other.hp
        kou = self.kou + other.kou
        bou = self.bou + other.bou
        tkou = self.tkou + other.tkou
        tbou = self.tbou + other.tbou
        suba = self.suba + other.suba
        s3 = Shuzokuchi(hp, kou, bou, tkou, tbou, suba)
        return s3

    # 減算
    def __sub__(self, other):
        hp = self.hp - other.hp
        kou = self.kou - other.kou
        bou = self.bou - other.bou
        tkou = self.tkou - other.tkou
        tbou = self.tbou - other.tbou
        suba = self.suba - other.suba
        s4 = Shuzokuchi(hp, kou, bou, tkou, tbou, suba)
        return s4

    # 自身が他方より大きい場合
    def __gt__(self, other):
        if self.sumstatus > other.sumstatus:
            return True
        else:
            return False

    # 自身が他方より小さい場合
    def __lt__(self, other):
        if self.sumstatus < other.sumstatus:
            return True
        else:
            return False

    # 自身と他方が等しい場合
    def __eq__(self, other):
        if self.sumstatus == other.sumstatus:
            return True
        else:
            return False


if __name__ == "__main__":
    try:
        p1 = [45, 49, 49, 65, 65, 45]  # フシギダネ
        s1 = Shuzokuchi(*p1)
        print(s1)
    except Exception as e:
        print(e)

    try:
        p2 = [39, 52, 43, 60, 50, 65]  # ヒトカゲ
        s2 = Shuzokuchi(*p2)
        print(s2)
    except Exception as e:
        print(e)

    try:
        s3 = s1+s2  # フシギダネとヒトカゲが合体
        print(s3)
    except Exception as e:
        print(e)

    try:
        s4 = s3-s2  # 合体ポケモンからヒトカゲが剥がれた
        print(s4)
    except Exception as e:
        print(e)

    try:
        print(s1["hp"], s2["hp"], s3["hp"], s4["hp"])

        print(s3 > s4, s3 < s4)
        print(s4 == s1)
    except Exception as e:
        print(e)

    try:
        s5 = s1-s2  # フシギダネーヒトカゲ
    except Exception as e:
        print(e)

    try:
        s0 = Shuzokuchi(*[0 for _ in range(6)])  # 全種族値が0のザコポケ
    except Exception as e:
        print(e)
