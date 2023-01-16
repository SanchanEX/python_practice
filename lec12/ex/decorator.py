from functools import wraps


def bossy(func):  # 偉そうなデコレータ
    @wraps(func)
    def _func(t):
        print("オレの名前は", end="")
        func(t)
        print("様だ！")
    return _func


def humble(func):  # 謙遜なデコレータ
    @wraps(func)
    def _func(t):
        print("わたくしの名前は", end="")
        func(t)
        print("でございます")
    return _func


@bossy
# @humble
def print_name(t):  # デコレート対象の関数
    print(t, end="")


print_name("ピカチュウ")  # 常にデコレートされた状態
print()


print(print_name.__name__, print_name)
