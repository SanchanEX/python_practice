import multiprocessing
import random
import sys
import time


def sampling(num):
    # print(num)
    cnt = 0.0
    for i in range(num):
        x = random.random()
        y = random.random()
        if x*x+y*y < 1.0:
            cnt += 1.0
    return cnt


if __name__ == "__main__":
    bgn = time.time()
    key = sys.argv[1]

    total = 100000000
    num = int(total/1000)
    nums = [num for _ in range(1000)]

    pl = multiprocessing.Pool(int(key))
    results = pl.map(sampling, nums)

    end = time.time()
    ans = 4.0 * sum(results) / total

    print(f"{sum(results)} / {total} = {ans:.8f}")
    print(f"所要時間: {end-bgn:.2f}秒")
