from array import array

lst = [1, 16, 129, 134, 246, 467]
ary = array('I', lst)

lst.append("道路")
print(lst)

ary.append("道路")
print(ary)
