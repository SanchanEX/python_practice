with open("../data_20220926/poke_names.txt", "r", encoding="utf8") as rfo:
    for row in rfo:
        print(row.rstrip())
