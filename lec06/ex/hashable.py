from pprint import pprint
a = 243
print(hash(a))
print(a.__hash__())

a = 172.5
print(hash(a))
print(a.__hash__())

a = "fsm"
print(hash(a))
print(a.__hash__())

a = (1, 2, 0, 1)
print(hash(a))
print(a.__hash__())

a = [1, 2, 0, 1]
# print(hash(a))
# print(a.__hash__())


class Monster:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title

    # def __eq__(self, other):
    #     return self.title == other.title

    # def __hash__(self):
    #     return hash(self.title)


# pprint(Monster.__dict__)

# a = Monster("ピカチュウ")
# print(hash(a), id(a))
# b = Monster("ピカチュウ")
# print(hash(b), id(b))

# dct = dict()
# dct[a] = "1匹目"
# pprint(dct)
# dct[b] = "2匹目"
# pprint(dct)
# c = Monster("フシギダネ")
# dct[c] = "3匹目"
# pprint(dct)