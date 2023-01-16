import sqlite3


def sum_stats(h, a, b, c, d, s):
    return h+a+b+c+d+s


if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    # (SQL内での関数名, 引数の数, 上で定義した関数)
    con.create_function("sum", 6, sum_stats)
    cur = con.cursor()
    cur.execute("SELECT sum(hp, atk, dfs, sp_atk, sp_dfs, spd) FROM stats")
    for row in cur.fetchall():
        print(row)
    con.close()
