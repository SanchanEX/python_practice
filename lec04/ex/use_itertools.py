import itertools

lst = list(range(1, 11))
for i in itertools.accumulate(lst):
    print(i, end=" ")
print()

titles = ["フシギダネ", "フシギソウ", "フシギバナ", "ヒトカゲ", "リザード", "リザードン", "ゼニガメ", "カメール", "カメックス"]
for title in itertools.accumulate(titles):
    print(title)

for key_, group_ in itertools.groupby(titles, key=lambda title: title[0:2]):
    print(f"{key_}：", end="\t")
    for title in group_:
        print(title, end=" ")
    print()

for title in itertools.islice(titles, 2, None, 3):
    print(title)

for tpl in itertools.product(titles, titles):
    print(tpl, end=" ")
print()

for tpl in itertools.permutations(titles, 2):
    print(tpl, end=" ")
print()

for tpl in itertools.combinations(titles, 3):
    print(tpl, end=" ")
print()
