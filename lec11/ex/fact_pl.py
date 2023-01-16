import math
import multiprocessing
import os
import time


if __name__ == "__main__":
    bgn = time.time()
    print(os.cpu_count())
    values = list(range(10000))
    pl = multiprocessing.Pool()
    results = pl.map(math.factorial, values)
    print(math.factorial)
    end = time.time()
    print("集計結果：", len(results))
    print(f"所要時間：{end-bgn:.2f}秒")
