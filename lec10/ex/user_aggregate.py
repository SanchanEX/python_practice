import sqlite3


class MaxAverage:
    def __init__(self):
        self.max = 0

    def step(self, *tpl):
        # 平均値
        avg = sum(tpl)/len(tpl)

        # 平均値の最大値
        if self.max < avg:
            self.max = avg

    def finalize(self):
        return self.max


if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    con.create_aggregate("max_avg", 6, MaxAverage)
    cur = con.cursor()
    cur.execute("SELECT max_avg(hp, atk, dfs, sp_atk, sp_dfs, spd) FROM stats")
    for row in cur:
        print(row)
    con.close()
