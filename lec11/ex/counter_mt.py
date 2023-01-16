import collections
import random
import time
import threading


def read_types(file_path):
    with open(file_path, encoding="utf8") as rfo:
        types = list()
        for row in rfo:
            col = row.rstrip().split("\t")
            types.append(col[2].split())
    return types


def counter(cnt_dct, type_):
    # 現在の辞書の値を抽出
    now = cnt_dct[type_]

    # 乱数のsleep
    rnd = random.randint(1, 5)
    print(f"{rnd}秒sleep")
    time.sleep(rnd)

    # 現在の値を更新
    cnt_dct[type_] = now+1
    print(f"{type_}を追加", cnt_dct)


if __name__ == "__main__":
    types = read_types("../data/poke_names.txt")

    # カウント用の空辞書
    cnt_dct = collections.defaultdict(int)

    # 辞書とタイプ文字列を返す
    for type_lst in types[:9]:
        for type_ in type_lst:
            th = threading.Thread(
                target=counter,
                args=(cnt_dct, type_)
            )
            th.start()

    for th in threading.enumerate():
        if th.name == "MainThread":
            continue
        th.join()   # スレッドが終了してから集計させるためのメソッド

    print("="*30)
    print("集計結果：", cnt_dct)    # 正しくない集計結果
