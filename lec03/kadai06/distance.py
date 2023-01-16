import sys
import pokemon


def calc_similar_monster(dist, mypoke):
    global poke

    result_min = 1000000

    for p in poke:
        if p == mypoke:
            continue

        result = dist(mypoke[0], p[0])

        if result < result_min:
            result_min = result
            result_minpoke = p

    return (result_minpoke, result_min)


if __name__ == "__main__":
    sts = pokemon.read_stats(sys.argv[1])
    names = pokemon.read_names(sys.argv[2])[0]
    poke = []
    for st, name in zip(sts, names):
        poke.append([st, name])
    mypoke = poke[int(sys.argv[3]) - 1]

    dist_dict = {"Manhattan": lambda lst_x, lst_y: sum(abs(x - y) for x, y in zip(lst_x, lst_y)),
                 "Eucidean": lambda lst_x, lst_y: (sum(abs(x - y)**2 for x, y in zip(lst_x, lst_y)))**0.5,
                 "Chebyshev": lambda lst_x, lst_y: max(abs(x - y) for x, y in zip(lst_x, lst_y))
                 }

    print(f'僕のポケモン:{mypoke[1]}')
    for i in dist_dict:
        p, dis = calc_similar_monster(dist_dict[i], mypoke)
        print(f'{i}距離:一番類似するのは{p[1]}で距離は{dis}')
