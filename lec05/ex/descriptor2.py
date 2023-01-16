from pprint import pprint

class PokeDesc:
    def __init__(self, attrname):
        self.attrname = attrname

    def __get__(self, obj, objtype=None):
        print(f'参照：{obj.__dict__[self.attrname]=}')
        return obj.__dict__[self.attrname]

    def __set__(self, obj, value):
        obj.__dict__[self.attrname] = value
        print(f'更新：{obj.__dict__[self.attrname]=}')


class Monster:
    title = PokeDesc("title")
    level = PokeDesc("level")

    def __init__(self, title):
        self.title = title


if __name__ == "__main__":
    fushi = Monster("フシギダネ")
    pika = Monster("ピカチュウ")
    fushi.level = 25
    print("-"*20)
    pprint(fushi.__dict__)
    print(fushi.title, fushi.level)
    print("-"*20)
    pprint(pika.__dict__)
    print(pika.title)
    print("-"*20)
    pprint(Monster.__dict__)


