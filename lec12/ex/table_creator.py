import sqlite3
import time


class TableCreator:
    def __init__(self, db_path):
        self.db_path = db_path  # DB名

    def __enter__(self):
        self.con = sqlite3.connect(self.db_path)
        print(f"{self.db_path}に接続しました")
        self.cur = self.con.cursor()
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

    def create(self, tbl_name, col_lst):
        self.tbl_name = tbl_name
        self.columns = ",".join(col_lst)

        try:
            sql = f"CREATE TABLE {self.tbl_name} ({self.columns})"
            self.cur.execute(sql)
        except sqlite3.OperationalError as e:
            print(f"[ERROR] {e}")
            self.cur.execute(f"DROP TABLE {self.tbl_name}")
            print(f"{self.tbl_name}を削除しました")

            time.sleep(1)
            print("処理中です.しばらくお待ちください...")

            i = 0
            while True:
                i += 1
                print(".")
                time.sleep(0.2)
                if i == 10:
                    break

            sql = f"CREATE TABLE {self.tbl_name} ({self.columns})"
            self.cur.execute(sql)

        print(f"{self.tbl_name}を構築しました")


if __name__ == "__main__":
    db_path = "../data/pokemon.db"
    tbl_name = "names"
    col_lst = ["id", "name", "types", "evolvs"]
    with TableCreator(db_path) as tc:
        tc.create(tbl_name, col_lst)
