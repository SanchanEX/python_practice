from pprint import pprint


class PokeDesc:
    def __get__(self, obj, objtype=None):
        print("参照")
        return self.value

    def __set__(self, obj, value):
        self.value = value
        print("更新")


class Monster:
    title = PokeDesc()
    level = PokeDesc()

    def __init__(self, title):
        self.title = title


if __name__ == "__main__":
    fushi = Monster("フシギダネ")
    pika = Monster("ピカチュウ")
    fushi.level = 25

    print("============================")
    pprint(fushi.__dict__)
    print(fushi.title, fushi.level)  # getが動く

    print("============================")
    pprint(pika.__dict__)
    print(pika.title)

    print("============================")
    pprint(Monster.__dict__)
