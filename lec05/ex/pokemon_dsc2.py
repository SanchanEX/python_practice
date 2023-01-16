class Title:
    def __init__(self, minval, maxval):
        self.maxval = maxval
        self.minval = minval

    def __set_name__(self, owner, attrname):
        self.attrname = attrname
        print(f"属性{self.attrname}のディスクリプタを設置")

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.attrname]

    def __set__(self, obj, value):
        self.validate(value)    # 値を検証
        obj.__dict__[self.attrname] = value

    def validate(self, value):
        if not (self.minval <= len(value) <= self.maxval):
            raise ValueError("文字数範囲規定違反")


class Level:
    def __init__(self, minval, maxval):
        self.maxval = maxval
        self.minval = minval

    def __set_name__(self, owner, attrname):
        self.attrname = attrname
        print(f"属性{self.attrname}のディスクリプタを設置")

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.attrname]

    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self.attrname] = 10

    def validate(self, value):
        if not (self.minval <= value <= self.maxval):
            raise ValueError("レベル範囲規定違反")


class Monster:
    title = Title(2, 5)
    level = Level(1, 100)

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
