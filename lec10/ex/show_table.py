import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM sqlite_master WHERE type='table'")
    for row in cur:
        print(row)
    con.close()
