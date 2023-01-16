if __name__ == "__main__":
    rfo = open("../data/poke_names.txt", encoding="utf-8")
    print(rfo, rfo.closed)
    print(dir(rfo))
    with rfo:
        for i, row in enumerate(rfo):
            row = row.rstrip()
            print(row)
            if i == 9:
                break
    print(rfo, rfo.closed)
