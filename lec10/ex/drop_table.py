import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("lec10/databases/pokemon.db")
    cur = con.cursor()
    cur.execute("DROP TABLE stats")
    con.close()
