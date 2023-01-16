import sqlite3
import sys


class SqlExecuter:
    def __init__(self, db_path, tbl_name, col_lst):
        self.db_path = db_path
        self.tbl_name = tbl_name
        self.col_lst = col_lst

    def __enter__(self):
        self.con = sqlite3.connect(self.db_path)
        print(f"{self.db_path}に接続しました")

        self.cur = self.con.cursor()

        try:
            self.cur.execute(f"CREATE TABLE {self.tbl_name} ({self.col_lst})")
            print(f"{self.tbl_name}を構築しました")
        except sqlite3.OperationalError as e:
            self.cur.execute(f"DROP TABLE {self.tbl_name}")
            self.cur.execute(
                f"CREATE TABLE {self.tbl_name} ({self.col_lst[0]}, {self.col_lst[1]}, {self.col_lst[2]}, {self.col_lst[3]})")
            print(f"{self.tbl_name}は既に存在していたので，一度削除してから構築しました")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("正常にSQLが実行されました")
            self.con.close()
            print("切断しました")
        else:
            print(f"正常にSQLが実行されませんでした")
            self.con.close()
            print("切断しました")

    def insert(self, names):
        self.cur.executemany(
            f"INSERT INTO {self.tbl_name} VALUES(?, ?, ?, ?)", names)
        self.con.commit()
        print("レコードを挿入しました")

    def select(self, colmun, condition, order):
        sql = f"SELECT {colmun} FROM {self.tbl_name} WHERE {condition} ORDER BY {order}"
        return self.cur.execute(sql)


def read_names(file_path):
    names = []
    with open(encoding="utf8", file=file_path, mode="r") as rfo:
        for row in rfo:
            id_, tit, typ, *evo_lst = row.rstrip().split("\t")
            evo = " ".join(evo_lst)
            names.append((int(id_), tit, typ, evo))
    return names


if __name__ == "__main__":
    names = read_names(sys.argv[1])  # "../data/poke_names.txt"
    db_path = sys.argv[2]  # "../data/pokemon.db"
    tbl_name = "names"
    col_lst = ["id", "name", "types", "evolvs"]
    with SqlExecuter(db_path, tbl_name, col_lst) as se:
        se.insert(names)
        rows = se.select("name", condition="id > 245", order="id DESC")
        for row in rows:
            print(row)
