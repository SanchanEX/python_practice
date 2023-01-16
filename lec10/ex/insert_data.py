import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("../databases/pokemon.db")
    cur = con.cursor()
    with open("../data/poke_names.txt", "r", encoding="utf8") as rfo:
        for row in rfo:
            code, title, types, *evolvs = row.rstrip().split("\t")
            evo = " ".join(evolvs)
            sql = f"INSERT INTO names VALUES({int(code)}, '{title}', '{types}', '{evo}')"
            print(sql)
            cur.execute(sql)
    con.commit()    # 確定させる
    con.close()
