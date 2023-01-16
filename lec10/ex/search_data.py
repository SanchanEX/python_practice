import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM names WHERE id > 240 ORDER BY id DESC")
    for row in cur:  # .fetchmany(5):
        print(row)  # [1])
    con.close()
