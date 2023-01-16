from pprint import pprint

stats = []
with open("../data/base_stats.txt", "r") as rfo:
    for row in rfo:
        row = row.rstrip()
        stats.append([int(col) for col in row.split(" ")])

stats.sort(key=lambda s: s[1], reverse=True)
#stats.sort(key=lambda s:sum(s), reverse=True)
for i, stat in enumerate(stats, 1):
    print(stat)
    if i == 5:
        break
