from pprint import pprint


class PokeDesc:
    def __set_name__(self, owner, attrname):
        self.attrname = attrname    # 属性の名前
        print(f"設置：{owner.__name__}の{self.attrname}")

    def __get__(self, obj, objtype=None):
        print(f'参照：{obj.__dict__[self.attrname]=}')
        return obj.__dict__[self.attrname]

    def __set__(self, obj, value):
        obj.__dict__[self.attrname] = value  # 直接代入
        print(f'更新：{obj.__dict__[self.attrname]=}')


class Monster:
    title = PokeDesc()
    level = PokeDesc()

    def __init__(self, title):
        self.title = title


if __name__ == "__main__":
    print("main開始")
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
