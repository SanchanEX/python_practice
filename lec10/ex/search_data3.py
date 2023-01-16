import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM names")
    for row in cur.fetchmany(5):
        print(row["name"])
    con.close()
