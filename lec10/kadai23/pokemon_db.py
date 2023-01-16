import sqlite3
import sys


def read_names(file_path):
    names = []
    with open(encoding="utf8", file=file_path, mode="r") as rfo:
        for row in rfo:
            id_, nam, typ, *evo_lst = row.rstrip().split("\t")
            evo = " ".join(evo_lst)
            names.append((int(id_), nam, typ, evo))
    return names


def read_stats(file_path):
    stats = []
    with open(file_path, "r") as rfo:
        for row in rfo:
            row = row.rstrip()
            stats.append([int(col) for col in row.split(" ")])
    return stats


if __name__ == "__main__":
    name = read_names(sys.argv[1])  # ../data/poke_names.txt
    stats = read_stats(sys.argv[2])  # ../data/base_stats.txt
    db_path = sys.argv[3]  # ../kadai23/pokemon.db

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE name_stats (id, name, type, evolvs)")

    except sqlite3.OperationalError:
        cur.execute("DROP TABLE name_stats")
        cur.execute("CREATE TABLE name_stats (id, name, type, evolvs)")

    cur.executemany("INSERT INTO name_stats VALUES(?, ?, ?, ?)", name)
    con.commit()

    for n in ('hp', 'atk', 'dfs', 'sp_atk', 'sp_dfs', 'spd'):
        cur.execute("ALTER TABLE name_stats ADD COLUMN "+n)

    for i, stat in enumerate(stats, 1):
        cur.execute(
            f"UPDATE name_stats SET hp=?, atk=?, dfs=?, sp_atk=?, sp_dfs=?, spd=? WHERE id=={i}", stat)
        con.commit()

    con.close()
