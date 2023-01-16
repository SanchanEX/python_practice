import sys
import re
import sqlite3

# C0A20047


def read_html(file_path):
    with open(file_path, "r", encoding="utf8") as rfo:
        html = rfo.read().replace("\n", "")
    datepattern = r"<th scope=\"row\".*?>(\d{4}年\d{1,2}月\d{1,2}日)</th>"
    pricepattern = r"<td.*?><span.*?><span .*?><span .*?>([0-9.,]{1,})</span></span></span></td>"
    pattern = re.compile(datepattern+pricepattern*6)
    stocks = list()
    for match in pattern.findall(html):
        stocks.append([match[0]]+[float(m.replace(",", ""))
                      for m in match[1:]])
    return stocks


class MaxAverage:
    def __init__(self):
        self.max = 0

    def step(self, d1, d2):
        mean = (d1 + d2) / 2
        if self.max < mean:
            self.max = mean

    def finalize(self):
        return self.max


if __name__ == "__main__":
    stock = read_html(sys.argv[1])  # lec10/data/ufj.html
    db_path = sys.argv[2]  # lec10/kadai24/stocks.db
    con = sqlite3.connect(db_path)
    con.create_aggregate('max_avg', 2, MaxAverage)
    cur = con.cursor()
    try:
        cur.execute(
            "CREATE TABLE ufj (date, hajimene, takane, yasune, owarine, dekidaka, owarine2)")

    except sqlite3.OperationalError:
        cur.execute("DROP TABLE ufj")
        cur.execute(
            "CREATE TABLE ufj (date, hajimene, takane, yasune, owarine, dekidaka, owarine2)")

    cur.executemany("INSERT INTO ufj VALUES(?, ?, ?, ?, ?, ?, ?)", stock)
    cur.execute("SELECT max_avg(hajimene, owarine) FROM ufj",)

    for row in cur.fetchall():
        print(row)

    # 以下は変更しないこと
    sql = f"SELECT hajimene, owarine, (hajimene+owarine)/2 FROM ufj"
    cur.execute(sql)
    for row in cur.fetchall():
        print(row)

    con.close()
