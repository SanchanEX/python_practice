from pokemon import Monster
from pprint import pprint

if __name__ == "__main__":
    print(f"{__file__}の{__name__}(ifの中)")
    m = Monster("ピカチュウ", "でんき", 30, [])
    pprint(Monster.__dict__)
    pprint(m.__dict__)
