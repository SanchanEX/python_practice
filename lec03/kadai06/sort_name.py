""" 
目標：ポケモンの名前を辞書順にソートする 
"""
import sys


def read_names(file_path):
    """ ポケモンの名前を操作する関数 """
    names, _, _ = [], [], []    # names, types, evolsを初期化して定義
    with open(encoding="utf8", file=file_path, mode="r") as rfo:    # file_pathに指定したファイルを開く
        for row in rfo:   # 1行ずつ取り出し，回す
            _, nam, _, *_ = row.rstrip().split("\t")    # タブで区切る, rstripで末尾削除
            names.append(nam)              # 名前をappend
    return names


def write_names(file_path, names):
    sorted_list = sorted(names)
    with open(encoding="utf8", file=file_path, mode="w", newline='\n') as wfo:
        for row in sorted_list:
            nam = row.rstrip()
            wfo.write(nam+'\n')


n = read_names(sys.argv[1])
write_names(sys.argv[2], n)
