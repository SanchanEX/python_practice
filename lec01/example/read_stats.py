from pprint import pprint

stats = []
with open("../data/base_stats.txt", "r") as rfo:
    for row in rfo:
        row = row.rstrip()
        stats.append([
            int(col)
            for col in row.split(" ")
        ])  # appendしたものをさらにappendするs => 2次元リスト


pprint(stats)
