from pprint import pprint

print(f"{__file__}の{__name__}(ifの外)")

class Monster:
    num_of_monsters = 0
    def __init__(self, title, type_, level, stats):
        print(f"{__class__.__name__}クラスの{__class__.__init__.__name__}関数")
        self.title = title
        self.type_ = type_
        self.level = level
        self.stats = stats
        __class__.num_of_monsters += 1


if __name__ == "__main__":
    print(f"{__file__}の{__name__}(ifの中)")
    m = Monster("ピカチュウ", "でんき", 30, [])
    pprint(Monster.__dict__)
    pprint(m.__dict__)
