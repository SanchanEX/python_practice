import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("lec10/databases/pokemon.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM stats")
    for row in cur.fetchmany(10):
        print(row)
    con.close()
