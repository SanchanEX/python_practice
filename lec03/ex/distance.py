def eucl_dist(lst_x, lst_y):
    s = 0.0
    for x, y in zip(lst_x, lst_y):
        s += (x-y)**2
    return s**0.5
    # return sum([(x-y)**2 for x, y in zip(lst_x, lst_y)])**0.5 # 内包表記版

fushi1 = [45, 49, 49, 65, 65, 45]
fushi2 = [60, 62, 63, 80, 80, 60]
print(eucl_dist(fushi1, fushi2))

print( (lambda lst_x, lst_y: sum([(x-y)**2 for x, y in zip(lst_x, lst_y)])**0.5)(fushi1, fushi2) )
