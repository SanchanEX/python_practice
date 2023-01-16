rfo = open("lec01/data/poke_names.txt", "r", encoding="utf8")
try:
    for row in rfo:
        print(row.rstrip())
finally:    # 例外発生時にクローズさせる
    rfo.close()

# compare with python with
# with open("../data_20220926/poke_names.txt", "r", encoding="utf8") as rfo:
#     for row in rfo:
#         print(row.rstrip())
