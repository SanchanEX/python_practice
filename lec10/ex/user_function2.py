import sqlite3


def balance(x, y):
    return (x+y)/2


if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    con.create_function("avg", 2, balance)
    cur = con.cursor()
    cur.execute("SELECT avg(atk, dfs) AS avg FROM stats ORDER BY avg DESC")
    for row in cur.fetchmany(10):
        print(row)
    con.close()
