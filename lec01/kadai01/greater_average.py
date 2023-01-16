import sys
from pprint import pprint


def read_stats(file_path):
    stats = []
    with open(file_path, "r") as f:
        for row in f:
            row = row.rstrip()  # 改行削除
            stats.append([
                int(col)
                for col in row.split(" ")
            ])
    # return print(stats)
    return stats    # 2次元リスト


def calc_average(lst):
    return sum(lst)/len(lst)


if __name__ == "__main__":
    stats = read_stats(sys.argv[1])

    sum_list = []
    sum_stat = 0
    for col_idx in range(251):
        sum_stat += sum(stats[col_idx])/6
    all_ave = sum_stat/251
    print(all_ave)

    l = [(i+1, stats[i])
         for i, j in enumerate(stats) if all_ave < calc_average(stats[i])]
    pprint(l, width=100)
