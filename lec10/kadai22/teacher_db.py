import sys
import re
import sqlite3


def read_html(file_path):
    with open(file_path, "r", encoding="utf8") as rfo:
        html = rfo.read().replace("\n", "")
    pattern = re.compile(
        r"<a href=\"(/info/lab/teacher/cs/index.html\?id=\d+).*?\">.*?<h2>(.*?)</h2>.*?<h4>(.*?)</h4>.*?<p>(.*?)</p>")
    match_lst = pattern.findall(html)
    teachers = []
    teacher_id = []
    for i, match in enumerate(match_lst, 1):
        name = match[1]
        url = "https://www.teu.ac.jp"+match[0]
        pos = match[2].split()[0]
        field = match[3]
        teachers.append((i, name, url, pos, field))
        # teacher_id.append(i)
    return teachers


if __name__ == "__main__":
    teachers = read_html(sys.argv[1])  # ../data/teachers.html
    db_path = sys.argv[2]  # ../kadai22/teachers.db

    con = sqlite3.connect(db_path)

    cur = con.cursor()
    try:
        cur.execute(
            "CREATE TABLE cs (id INTEGER, name TEXT, url TEXT, position TEXT, fields TEXT)")
    except sqlite3.OperationalError as e:
        cur.execute("DROP TABLE cs")
        cur.execute(
            "CREATE TABLE cs (id INTEGER, name TEXT, url TEXT, position TEXT, fields TEXT)")

    sql = f"INSERT INTO cs VALUES(?, ?, ?, ?, ?)"
    cur.executemany(sql, teachers)

    con.commit()
    con.close()
