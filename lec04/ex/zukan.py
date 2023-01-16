import sys

class Zukan:
    def __init__(self, file_path):
        self.titles = __class__.read_file(file_path)
        

    def __iter__(self):
        

    def __next__(self):
        if self.idx == len(self.titles):
            raise StopIteration()
        
        
        return title

    # def __getitem__(self, idx):
    #     if idx < 0 or len(self.titles) <= idx:
    #         raise IndexError()
    #     return self.titles[idx]
    
    @staticmethod
    def read_file(file_path):
        titles = []
        with open(file_path, "r", encoding="utf8") as rfo:
            for row in rfo:
                _, tit, _, *_ = row.rstrip().split("\t")
                titles.append(tit)
        return titles
    

if __name__ == "__main__":
    zukan = Zukan(sys.argv[1]) # lec04/data/poke_names.txt
    print(next(zukan))
    print(next(zukan))
    for i, z in enumerate(zukan, 1):
        print(f"{i:03d}\t{z}")
        if i == 5:
            break

    for i, z in enumerate(zukan, 1):
        print(f"{i:03d}\t{z}")
        if i == 5:
            break

    print(zukan[132])
