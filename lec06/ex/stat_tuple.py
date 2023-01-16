from pprint import pprint

def read_stats(file_path):
    stats = []
    with open(file_path, "r") as rfo:
        for row in rfo:
            row = row.rstrip()
            stats.append([int(col) for col in row.split(" ")])
    return stats


if __name__ == "__main__":
    stats = read_stats("lec06/data/base_stats.txt")
    field_names = ["H", "A", "B", "C", "D", "S"]
    tpls = []
    for stat in stats:

        tpls.append(tpl)
    pprint(tpls)
    