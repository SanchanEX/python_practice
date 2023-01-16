import functools
import multiprocessing
import random
import sys
import time


def time_measure(func):
    # print(func)
    @functools.wraps(func)
    def _func(*args):
        bgn = time.time()
        # print(func(*args))
        res = func(*args)
        end = time.time()
        print(f"所要時間: {end-bgn:.2f}秒")
        return res
    return _func


@time_measure
def sampling(num):
    cnt = 0
    for _ in range(num):
        x = random.random()
        y = random.random()
        if x**2+y**2 < 1:
            cnt += 1
    return cnt


if __name__ == "__main__":
    bgn0 = time.time()

    total = 100000000
    num = int(total/100)
    nums = [num for _ in range(100)]

    num_of_processes = int(sys.argv[1])

    pl = multiprocessing.Pool(num_of_processes)
    results = pl.map(sampling, nums)

    print(f"{4.0*sum(results)}/{total} = {4.0*sum(results)/total}")

    end0 = time.time()
    print(f"所要時間: {end0-bgn0:.2f}秒")
