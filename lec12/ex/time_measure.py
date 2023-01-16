import time


def time_measure(func):
    def _func(*args):
        bgn = time.time()
        func(*args)
        end = time.time()
        print(f"所要時間: {end-bgn:.2f}秒")
        print("="*30)
    return _func


@time_measure
def str_concat1(num):
    s = ""
    for i in range(num):
        s += str(i)
    return s


@time_measure
def str_concat2(num):
    s = "".join([str(i) for i in range(num)])
    return s


if __name__ == "__main__":
    str_concat1(1000000)
    str_concat2(1000000)
