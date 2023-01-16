from pokemon import *
from random import randint, choice
import sys

if __name__ == "__main__":
    names = read_names(sys.argv[1]) # .\lec02\data\poke_names.txt
    stats = read_stats(sys.argv[2]) # .\lec02\data\base_stats.txt
    monsters = [Monster(n, s) for n, s in zip(names, stats)]
    for mon in monsters:
        mon.level = randint(-10, 100) # 全ポケモンに対して，レベルを乱数で設定する
    ## ここまでが準備

    my_monster = monsters[int(sys.argv[3])-1] # 自分のパートナーポケモン
    print("僕のポケモン：", my_monster)

    for _ in range(5):
        teki = choice(monsters)
        print("vs", teki)
        if my_monster > teki:
            print(my_monster, "の勝ち！")
        else:
            print(my_monster, "の負け(>_<)")
