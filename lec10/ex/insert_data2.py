import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    cur = con.cursor()
    with open("../data/base_stats.txt", "r") as rfo:
        stats = []
        for row in rfo:
            stat = row.rstrip().split()
            stats.append([int(s) for s in stat])

    sql = f"INSERT INTO stats VALUES(?, ?, ?, ?, ?, ?)"
    cur.executemany(sql, stats)
    con.commit()

    con.close()
