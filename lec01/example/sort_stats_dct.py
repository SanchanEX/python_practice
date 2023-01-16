from pprint import pprint

stats = []  # 1次元リスト
key_list = ["hp", "attack", "defense",
            "sp_atk", "sp_def", "speed"]

with open("../data/base_stats.txt", "r") as rfo:
    for row in rfo:
        cols = row.rstrip().split(" ")
        stats.append({key: int(col)
                      for col, key in zip(cols, key_list)})

stats.sort(key=lambda s: s["attack"],  # 辞書のキー列でソート
           reverse=True)
for i, stat in enumerate(stats, 1):
    print(stat)
    if i == 5:  # 上位5件のみ
        break
