class Title:
    def __set_name__(self, owner, attrname):
        self.attrname = attrname
        print(f"属性{self.attrname}のディスクリプタを設置")

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.attrname]

    def __set__(self, obj, value):
        obj.__dict__[self.attrname] = value


class Level:
    def __set_name__(self, owner, attrname):
        self.attrname = attrname
        print(f"属性{self.attrname}のディスクリプタを設置")

    def __get__(self, obj, objtype=None):
        return 10

    def __set__(self, obj, value):
        obj.__dict__[self.attrname] = value


class Monster:
    title = Title()
    level = Level()

    def __init__(self, title, level):
        self.title = title
        self.level = level

    def __repr__(self):
        return f"{self.title}(Lv.{self.level})"


if __name__ == "__main__":
    fushi = Monster("フシギダネ", 20)
    print(fushi, fushi.__dict__)
    pika = Monster("ピカチュウ", -15)
    print(pika, pika.__dict__)
    muu = Monster("ミュースリー", 100)
    print(muu, muu.__dict__)
