import sys

class Zukan:
    def __init__(self, file_path):
        self.titles = __class__.read_file(file_path)

    def __iter__(self):
        return ZukanIterator(self)

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
    zukan = Zukan(sys.argv[1]) # lec04/data/poke_names.txt
    # print(next(zukan)) # イテレータではない（__next__()を持っていない）ため，
    # print(next(zukan)) # next()関数により__next__()を呼び出せない
    for i, z in enumerate(zukan, 1):
        print(f"{i:03d}\t{z}")
        if i == 5:
            break

    for i, z in enumerate(zukan, 1):
        print(f"{i:03d}\t{z}")
        if i == 5:
            break