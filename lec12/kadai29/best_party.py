from itertools import combinations
import sys
import multiprocessing
import time


class Monster:
    def __init__(self, title, stats):
        self.title = title
        self.stats = stats

    def __repr__(self):
        return self.title


def read_files(file_path1, file_path2):
    titles = []
    with open(file_path1, "r", encoding="utf8") as rfo:
        for row in rfo:
            _, tit, _, *_ = row.rstrip().split("\t")
            titles.append(tit)

    stats = []
    with open(file_path2, "r") as rfo:
        for row in rfo:
            row = row.rstrip()
            stats.append([int(col) for col in row.split(" ")])

    monsters = [Monster(title, stat) for title, stat in zip(titles, stats)]
    # print(monsters)
    return monsters


def party_score(tpl):
    s = 0
    for mon in tpl:
        s += sum(mon.stats)
    return s


def max_party(lst):
    max_val = 0
    arg_max = None
    for tpl in lst:
        val = party_score(tpl)
        if val > max_val:
            arg_max = tpl
            max_val = val
    return max_val, arg_max


if __name__ == "__main__":
    bgn = time.time()
    monsters = read_files(sys.argv[1], sys.argv[2])

    # ここから

    poke_lst, sub_party = [], []
    i = 0
    for tpl in combinations(monsters, 3):
        i += 1
        poke_lst.append(tpl)
        if i % 10375 == 0:
            sub_party.append(poke_lst)
            poke_lst = []

    num_of_processes = int(sys.argv[3])
    pl = multiprocessing.Pool(num_of_processes)
    results = pl.map(max_party, sub_party)

    max_total = 0
    for total, team in results:
        if total > max_total:
            max_total = total
            strongest_team = team
    print(strongest_team)

    # ここまで

    end = time.time()
    print(f"所要時間:{end-bgn:.2f}")
