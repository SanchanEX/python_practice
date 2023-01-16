from pprint import pprint

def read_stats(file_path):
    stats = []
    with open(file_path, "r") as rfo:
        for row in rfo:
            row = row.rstrip()
            stats.append([int(col) for col in row.split(" ")])
    return stats

@dataclass
class Stat:


    # def __getitem__(self, key):
    #     return self.__dict__[key]

    def __add__(self, other):

    def __sub__(self, other):

    
if __name__ == "__main__":
    stats = read_stats("lec06/data/base_stats.txt")
    dcls = []
    for stat in stats:

        dcls.append(dcl)
    pprint(dcls)

    print(dcls[0]+dcls[3]) # 0:フシギダネ+3:ヒトカゲ   