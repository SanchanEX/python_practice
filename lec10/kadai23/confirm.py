import sqlite3
import sys

if __name__ == "__main__":
    db_path = sys.argv[1] # lec10/kadai23/pokemon.db
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = f"SELECT count(*) FROM name_stats"
    cur.execute(sql)
    row = cur.fetchone()
    print(row)
    print()

    sql = f"SELECT * FROM name_stats ORDER BY id LIMIT 10"
    cur.execute(sql)
    for row in cur:
        print(row)
    print()

    sql = f"SELECT * FROM name_stats WHERE id > 240"
    cur.execute(sql)
    for row in cur:
        print(row)

    con.close()
