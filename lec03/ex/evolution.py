from pokemon import *
import sys


def make_evolution(target):
    """ クロージャを生成 """
    def _evolve():
        nonlocal target
        evo_name = target.evolve()
        for mon in monsters:
            if mon.title == evo_name:
                target = mon
    return _evolve


def sum_params(mon):
    return (len(mon.evols)
            + len(mon.attacks)
            + len(mon.defenses))


def eucl_dist(lst_x, lst_y):
    return sum([(x-y)**2 for x, y in zip(lst_x, lst_y)])**0.5


if __name__ == "__main__":
    # names, types, evols = read_names(sys.argv[1])   # 第1引数に読み込むファイル
    stats, names, types, evols = read_files(sys.argv[1], sys.argv[2])
    # print(stats, names, types, evols)   # 全てprint
    monsters = [Monster(title) for title in names]  # ポケモンの名前を内包表記で1つずつ取得

    # print("==============================")
    # print(monsters[24])

    for mon, typ, evo in zip(monsters, types, evols):
        # zip(Monsterクラスのインスタンスのリスト，タイプリストのリスト，進化先リストのリスト)
        mon.set_types(*typ)  # 1 or 複数のタイプをセット
        mon.set_evols(*evo)  # 進化先をセット

    for mon in monsters:
        # ポケモンのリストを回し，タイプと進化先をprint
        # print(mon, mon.type_, mon.evols)
        print(mon.type_, mon.evols)

    pika = monsters[24]     # ピカチュウ
    shinka, kougeki, bougyo = Monster.evolve, Monster.attack, Monster.defense
    funcs = [shinka, kougeki, bougyo]
    pika.attacks.append("でんきショック")   # ピカチュウの技に追加
    pika.attacks.append("かみなり")        # ピカチュウの技に追加
    for f in funcs:
        f(pika)

    fushi = monsters[0]  # フシギダネ
    print(f"{fushi}：")

    res = sorted(monsters,
                 key=lambda mon: (len(mon.evols)
                                  + len(mon.attacks)
                                  + len(mon.defenses)),
                 reverse=True
                 )
    res = sorted(monsters, key=sum_params, reverse=True)

    fushi1 = [45, 49, 49, 65, 65, 45]
    fushi2 = [60, 62, 63, 80, 80, 60]
    print(eucl_dist(fushi1, fushi2))
    print((lambda lst_x, lst_y: sum(
        [(x-y)**2 for x, y in zip(lst_x, lst_y)])**0.5)(fushi1, fushi2))
