def read_stats(file_path):
    stats = []
    with open(file_path, "r") as rfo:
        for row in rfo:
            row = row.rstrip()
            stats.append([int(col) for col in row.split(" ")])
    return stats

def read_names(file_path):
    names, types, evols = [], [], []
    with open(encoding="utf8", file=file_path, mode="r") as rfo:
        for row in rfo:
            _, nam, typ, *evo = row.rstrip().split("\t")
            names.append(nam)              # 名前の文字列をappend 
            types.append(typ.split(" "))   # タイプのリストをappend
            evols.append([e for e in evo]) # 進化先のリストをappend

    return names, types, evols


class Monster:
    def __init__(self, title):
        self.title = title
        self.stats = []
        
    def __repr__(self):
        return self.title

