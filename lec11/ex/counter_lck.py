import collections
import random
import time
import threading
from threading import Lock


def read_types(file_path):
    with open(file_path, encoding="utf8") as rfo:
        types = list()
        for row in rfo:
            col = row.rstrip().split("\t")
            types.append(col[2].split())
    return types


def counter(cnt_dct, type_, lck):
    # ロック
    lck.acquire()

    now = cnt_dct[type_]
    rnd = random.randint(1, 5)
    print(f"{rnd}秒sleep")
    time.sleep(rnd)
    cnt_dct[type_] = now+1

    # ロック解除
    lck.release()
    print(f"{type_}を追加", cnt_dct)


if __name__ == "__main__":
    # lockオブジェクトを作成
    lck = Lock()

    types = read_types("../data/poke_names.txt")
    cnt_dct = collections.defaultdict(int)

    for type_lst in types[:9]:
        for type_ in type_lst:
            th = threading.Thread(
                target=counter,
                args=(cnt_dct, type_, lck)
            )
            th.start()

    for th in threading.enumerate():
        if th.name == "MainThread":
            continue
        th.join()   # スレッドが終了してから集計させるためのメソッド

    print("="*30)
    print("集計結果：", cnt_dct)    # 正しい集計結果
