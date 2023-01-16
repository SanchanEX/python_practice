rfo = open("../data_20220926/poke_names.txt", "r", encoding="utf8")
for row in rfo:     # ファイルオブジェクトから1行ずつ取り出す
    row = row.rstrip()
    if row:
        print(row)
    else:
        break
rfo.close()
