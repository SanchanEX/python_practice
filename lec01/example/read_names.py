import sys

file_path = sys.argv[1]
m = int(sys.argv[2])

with open(file_path, "r") as rfo:
    for i, row in enumerate(rfo, 1):
        row = row.rstrip()
        if i % m == 0:
            print(row)
