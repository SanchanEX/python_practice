from collections.abc import Iterable, Iterator, Sized, Container, Sequence

class Pokemon:
    pass


class Zukan:
    def __init__(self, file_path):
        self.titles = __class__.read_file(file_path)

    def __iter__(self):
        return ZukanIterator(self)

    def __getitem__(self, idx):
        return self.titles[idx]

    def __len__(self):
        return len(self.titles)

    @staticmethod
    def read_file(file_path):
        titles = []
        with open(file_path, "r", encoding="utf8") as rfo:
            for row in rfo:
                _, tit, _, *_ = row.rstrip().split("\t")
                titles.append(tit)
        return titles
    
    
class ZukanIterator():
    def __init__(self, zukan):
        self.source = zukan
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.source.titles):
            raise StopIteration()
        title = self.source.titles[self.idx]
        self.idx += 1
        return title


if __name__ == "__main__":
    zukan = Zukan("lec06/data/poke_names.txt")

    print(issubclass(Zukan, Pokemon))   # False
    print(issubclass(Zukan, list))      # False
    print(issubclass(Zukan, Iterable))  # True
    print("-"*20)
    print(isinstance(zukan, Zukan))     # True
    print(isinstance(zukan, list))      # False
    print(isinstance(zukan, Iterable))  # True
    print(isinstance(zukan, Iterator))  # False
    print(isinstance(zukan, Sized))     # False
    print(isinstance(zukan, Sequence))  # False
    print(isinstance(zukan, Container)) # False
    print("-"*20)
    print("__iter__", hasattr(Zukan, "__iter__"))
    print("__next__", hasattr(Zukan, "__next__"))
    print("__len__", hasattr(Zukan, "__len__"))
    print("__getitem__", hasattr(Zukan, "__getitem__"))
    print("__contains__", hasattr(Zukan, "__contains__"))
    print("-"*20)

    #zukan = 5
    # if isinstance(zukan, (list, tuple, dict, set, range, str, Zukan)):
    #     for item in zukan:
    #         print(item)

    #zukan = 5
    # try:
    #     for item in zukan:
    #         print(item)
    # except TypeError as e:
    #     print(e)

    #zukan = 5
    # if hasattr(zukan, "__iter__"):
    #     for item in zukan:
    #         print(item)

    #zukan = 5
    # if isinstance(zukan, Iterable):
    #     for item in zukan:
    #         print(item)
