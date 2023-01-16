import sqlite3
import sys

if __name__ == "__main__":
    db_path = sys.argv[1] # lec10/kadai22/teachers.db
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = f"SELECT count(*) FROM cs"
    cur.execute(sql)
    row = cur.fetchone()
    print(row)
    print()

    sql = f"SELECT * FROM cs ORDER BY id LIMIT 10"
    cur.execute(sql)
    for row in cur:
        print(row)
    print()

    sql = f"SELECT * FROM cs WHERE id > 28"
    cur.execute(sql)
    for row in cur:
        print(row)

    con.close()
