import collections
import random
import threading
import time


def read_types(file_path):
    with open(file_path, encoding="utf8") as rfo:
        types = list()
        for row in rfo:
            col = row.rstrip().split("\t")
            types.append(col[2].split())
    return types


def counter(cnt_dct, type_, smp):
    with smp:
        now = cnt_dct[type_]
        rnd = random.randint(1, 5)
        print(f"{rnd}秒sleep")
        time.sleep(rnd)
        cnt_dct[type_] = now+1
        print(f"{type_}を追加", cnt_dct)


if __name__ == "__main__":
    types = read_types("../data/poke_names.txt")
    cnt_dct = collections.defaultdict(int)
    smp = threading.Semaphore(1)

    for type_lst in types[:9]:
        for type_ in type_lst:
            th = threading.Thread(
                target=counter,
                args=(cnt_dct, type_, smp)
            )
            th.start()

    for th in threading.enumerate():
        if th.name == "MainThread":
            continue
        th.join()

    print("="*30)
    print("集計結果：", cnt_dct)
