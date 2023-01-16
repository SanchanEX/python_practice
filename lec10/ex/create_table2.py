
import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE stats (hp, atk, dfs, sp_atk, sp_dfs, spd)")

    con.close()
