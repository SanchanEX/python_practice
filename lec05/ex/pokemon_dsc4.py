from abc import ABC, abstractmethod


# 抽象クラス
class Validator(ABC):
    def __init__(self, minval, maxval):
        self.minval, self.maxval = minval, maxval

    def __set_name__(self, owner, attrname):
        self.attrname = attrname
        print(f"属性{self.attrname}のディスクリプタを設置")

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.attrname]

    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self.attrname] = value

    # 抽象メソッド
    @abstractmethod
    def validate(self, value):
        pass


class Title(Validator):
    def validate(self, value):
        if not (self.minval <= len(value) <= self.maxval):
            raise ValueError("文字数範囲規定違反")


class Level(Validator):
    def validate(self, value):
        if not (self.minval <= value <= self.maxval):
            raise ValueError("レベル範囲規定違反")


class Monster:
    title = Title(2, 5)
    level = Level(1, 100)
    # title = Validator(2, 5)
    # level = Validator(1, 100)

    def __init__(self, title, level):
        self.title = title
        self.level = level

    def __repr__(self):
        return f"{self.title}(Lv.{self.level})"


if __name__ == "__main__":
    fushi = Monster("フシギダネ", 20)
    print(fushi)
    pika = Monster("ピカチュウ", -15)
    print(pika)
    muu = Monster("ミュースリー", 100)
    print(muu)
