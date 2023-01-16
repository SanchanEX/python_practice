from pprint import pprint

stats = []  # 1次元リスト
key_list = ["hp", "attack", "defense",
            "sp_atk", "sp_def", "speed"]

with open("../data/base_stats.txt", "r") as rfo:
    for row in rfo:
        cols = row.rstrip().split(" ")
        stats.append({key: int(col)
                      for col, key in zip(cols, key_list)})

pprint(stats, width=100)
