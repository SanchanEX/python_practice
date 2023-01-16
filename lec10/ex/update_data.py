import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    cur = con.cursor()

    # idが1のレコードのnameをフシミダネに更新
    cur.execute("UPDATE names SET name='フシミダネ' WHERE id == 1")

    # idが2のレコードnameをフシミソウに更新
    cur.execute("UPDATE names SET name=? WHERE id == 2", ("フシミソウ", ))
    con.commit()
    con.close()
