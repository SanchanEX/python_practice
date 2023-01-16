import time


class time_measure:
    def __init__(self, func):
        # print("__init__")
        self.func = func

    def __call__(self, *args):
        bgn = time.time()
        # print("__call__")
        s = self.func(*args)
        end = time.time()
        print(f"所要時間：{end-bgn:.2f}秒")
        print("="*20)
        return s


# print("before @")
@time_measure
def str_concat1(num):
    # print("def 1")
    s = ""
    for i in range(num):
        s += str(i)
    return s
# print("after def")


# print("before @")
@time_measure
def str_concat2(num):
    # print("def 2")
    s = "".join([str(i) for i in range(num)])
    return s
# print("after def")


if __name__ == "__main__":
    # print("__main__")
    str_concat1(1000000)
    str_concat2(1000000)
