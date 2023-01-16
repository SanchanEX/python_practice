def fnc_square_even(stop):
    lst = []
    for i in range(stop):
        if i%2 == 0:
           lst.append(i*i)
    return lst


def gen_square_even(stop):
    for i in range(stop):
        if i%2 == 0:
            yield i*i

   
if __name__ == "__main__":
    print(fnc_square_even)
    lst = fnc_square_even(5)
    print(lst, len(lst))
    for item in lst:
        print(item)

    print("-"*20)
    print(gen_square_even)
    itr = gen_square_even(5)
    print(itr, itr) # len(itr)  # list(itr)
    for item in itr:
        print(item)


    # print("-"*20)
    # itr = gen_square_even(5)
    # item = next(itr)
    # print(item)
    # item = next(itr)
    # print(item)
    # item = next(itr)
    # print(item)
    # item = next(itr)
    # print(item)


    # print("-"*20)
    # gen = (i*i for i in range(5) if i%2 == 0) # ジェネレータ式
    # print(gen)
    # for item in gen:
    #     print(item)