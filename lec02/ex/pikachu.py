class Pikachu():
    title = "ピカチュウ"

    def __init__(self, level):
        self.level = level

    def __gt__(self, other):
        return self.level > other.level


class WildPikachu(Pikachu):
    num = 0
    title = "野生のピカチュウ"

    def __init__(self, level):
        super().__init__(level)  # 親クラスのイニシャライザでlevelを設定
        self.name = f"{__class__.title}その{__class__.num+1}"
        __class__.num += 1

    def __str__(self):          # 文字列化
        return f"{self.name}(Lv.:{self.level})"


class TamePikachu(Pikachu):
    def __init__(self, name, partner, level):
        self.name = name
        self.partner = partner
        super().__init__(level)

    def __str__(self):
        return f"{self.partner}の{self.name}(Lv.:{self.level})"
