import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    cur = con.cursor()

    # idが100以上のレコードを削除
    cur.execute("DELETE FROM names WHERE id >= 100")
    con.commit()
    con.close()
