import time

class time_measure:
    def __init__(self, func):
        print("time_measure __init__")
        self.func = func

    def __get__(self, obj, objtype=None):
        print("time_measure __get__")
        def _func(*args):
            print("def _func")
            bgn = time.time()
            print(self.func)
            print(self.func.__get__(obj, objtype))
            s  = self.func.__get__(obj, objtype)(*args)
            end = time.time()
            print(f"所要時間：{end-bgn:.2f}秒")
            print("#"*20)
            return s
        print("after _func", _func)
        return _func


class String:
    print("before @ 1")
    @time_measure
    def str_concat1(self, num):
        print("def 1")
        s = ""
        for i in range(num):
            s += str(i)
        return s
    print("after def 1")


    print("before @ 2")
    @time_measure
    def str_concat2(self, num):
        print("def 2")
        s = "".join([str(i) for i in range(num)])
        return s
    print("after def 2")


if __name__ == "__main__":
    print("__main__")
    s = String()
    s.str_concat1(1000000)
    s.str_concat2(1000000)