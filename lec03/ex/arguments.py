a, b, *c = [0, 1, 2, 3, 4]
print(c)


a, *b, c = (0, 1, 2, 3, 4)
print(b)


*a, b, c = "ABCDE"
print(a)
