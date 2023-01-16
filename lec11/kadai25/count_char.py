import collections
import sys
import threading

import time


def read_names(file_path):
    with open(file_path, encoding="utf8") as rfo:
        names = list()
        for row in rfo:
            col = row.rstrip().split("\t")
            names.append(col[1])
    return names


def counter(cnt_dct, name, smp):
    with smp:
        for n in name:
            cnt_dct[n] += 1


if __name__ == "__main__":
    names = read_names(sys.argv[1])  # "../data/poke_names.txt"
    cnt_dct = collections.defaultdict(int)
    smp = threading.Semaphore(10)

    for name in names:
        th = threading.Thread(
            target=counter,
            args=(cnt_dct, name, smp)
        )
        th.start()
        # counter(cnt_dct, name)

    for th in threading.enumerate():
        if th.name == "MainThread":
            continue
        th.join()

    sorted_dct = sorted(
        cnt_dct.items(), key=lambda item: item[1], reverse=True)
    print(f"集計結果：({len(sorted_dct)}種)", sorted_dct)
