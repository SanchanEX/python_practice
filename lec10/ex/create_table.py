import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    cur = con.cursor()
    # テーブルの作成
    # cur.execute("CREATE TABLE names (id INTEGER, name TEXT, types TEXT)")
    # cur.execute("DROP TABLE names")     # テーブルの削除
    # cur.execute("ALTER TABLE names ADD COLUMN evolvs TEXT")  # カラムの追加
    # cur.execute("ALTER TABLE names RENAME TO namae")    # テーブル名の変更
    con.close()
