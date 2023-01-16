from abc import ABC, abstractmethod

types = {"ノーマル", "ほのお", "みず",
         "くさ", "でんき", "こおり",
         "かくとう", "どく", "じめん",
         "ひこう", "エスパー", "むし",
         "いわ", "ゴースト", "ドラゴン",
         "あく", "はがね", "フェアリー"}


class Validator(ABC):
    def __set_name__(self, owner, attername):
        self.attername = attername

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.attername]

    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self.attername] = value

    @abstractmethod
    def validate(self, value):
        pass


class Title(Validator):
    def __init__(self, minval, maxval):
        self.minval = minval
        self.maxval = maxval

    def validate(self, value):
        if not (self.minval <= len(value) <= self.maxval):
            raise ValueError("文字数規定違反")


class Level(Validator):
    def __init__(self, minval, maxval):
        self.minval = minval
        self.maxval = maxval

    def validate(self, value):
        if not (self.minval <= value <= self.maxval):
            raise ValueError("レベル規定違反")


class Type(Validator):
    def __init__(self, val1):
        self.types1 = val1

    def validate(self, value):
        if value:
            if not value in types:
                raise ValueError("タイプ規定違反")
        else:
            pass


class Monster:
    title = Title(2, 5)
    level = Level(1, 100)
    types1 = Type(types)
    types2 = Type(types)

    def __init__(self, title, level, types1, *types2):
        self.title = title
        self.level = level
        self.types1 = types1
        if types2:
            self.types2 = types2[0]
        else:
            self.types2 = ()

    def __repr__(self) -> str:
        if self.types2:
            return f"{self.title}(Lv.{self.level}) 【{self.types1} {self.types2}】"
        else:
            return f"{self.title}(Lv.{self.level}) 【{self.types1}】"


if __name__ == "__main__":
    try:
        fushi = Monster("フシギダネ", 20, "くさ", "どく")
        print(fushi)
    except Exception as e:
        print(e)

    try:
        pika = Monster("ピカチュウ", -15, "でんき")
        print(pika)
    except Exception as e:
        print(e)

    try:
        eevee = Monster("イーブイ", 25, "いろいろ")
        print(eevee)
    except Exception as e:
        print(e)

    try:
        muu = Monster("ミュースリー", 100, "エスパー")
        print(muu)
    except Exception as e:
        print(e)
