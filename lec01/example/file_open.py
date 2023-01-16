rfo = open("../data_20220926/poke_names.txt", "r")
while True:
    row = rfo.readline().rstrip()  # 1行ずつ読み込み
    if row:  # rowが存在すれば
        print(row)
    else:
        break
rfo.close()
