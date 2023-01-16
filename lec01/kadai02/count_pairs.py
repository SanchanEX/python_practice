from pprint import pprint
import sys

with open(sys.argv[1], "r") as f:
    multiple_types = [
        tuple(
            p_f.rstrip().split()[2:]
        ) for p_f in f
        if len(p_f.rstrip().split()) == 4
    ]

dic = {}

for multiple_type in multiple_types:
    if not multiple_type in dic:
        dic[multiple_type] = 1
    else:
        dic[multiple_type] += 1

pprint(sorted(dic.items(), key=lambda t: t[1], reverse=True))
