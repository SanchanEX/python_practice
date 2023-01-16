import collections
import random
import time
import threading
import multiprocessing


def read_types(file_path):
    with open(file_path, encoding="utf8") as rfo:
        types = list()
        for row in rfo:
            col = row.rstrip().split("\t")
            types.append(col[2].split())
    return types


def counter(cnt_dct, type_, pp):
    # 現在の辞書の値を抽出
    now = cnt_dct[type_]

    # 乱数のsleep
    rnd = random.randint(1, 5)
    print(f"{rnd}秒sleep")
    time.sleep(rnd)

    # 現在の値を更新
    cnt_dct[type_] = now+1

    pp.send(cnt_dct)
    pp.close()

    print(f"{type_}を追加", cnt_dct)


if __name__ == "__main__":
    types = read_types("../data/poke_names.txt")

    # カウント用の空辞書
    cnt_dct = collections.defaultdict(int)
    processes = list()

    # 辞書とタイプ文字列を返す
    for type_lst in types[:9]:
        for type_ in type_lst:
            pp1, pp2 = multiprocessing.Pipe()
            pr = multiprocessing.Process(
                target=counter,
                args=(cnt_dct, type_, pp1),
            )
            pr.start()
            cnt_dct = pp2.recv()    # メインプロセスはサブプロセスから辞書を受け取り，cnt_dctは最新の状態
            processes.append(pr)

    for pr in processes:
        pr.join()

    print("="*30)
    print("集計結果：", cnt_dct)    # 集計されていない
