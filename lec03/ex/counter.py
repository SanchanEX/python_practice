def make_counter():
    cnt = 0
    print("カウンタ関数を作成します")

    def counter():
        nonlocal cnt
        cnt += 1
        return f"回数：{cnt}"

    return counter


def counter():
    cnt = 0
    cnt += 1
    return f"回数：{cnt}"


cnt = 20
counter1 = make_counter()
print(counter1())
print(counter1())
print(counter1())

counter2 = make_counter()
print(counter2())
print(counter1())

print(counter())
print(counter())
print(counter())

