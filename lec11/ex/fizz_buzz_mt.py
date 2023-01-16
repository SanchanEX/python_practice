from threading import Thread
import time
import threading


def fizz_buzz(num, bgn0):
    bgn = time.time()
    print(f"fizz_buzz start：{num}")
    result_lst = []
    for i in range(1, num+1):
        result = ""
        if i % 3 == 0:
            result += "fizz"
        if i % 5 == 0:
            result += "buzz"
        if result == "":
            result = str(i)
        result_lst.append(result)
    end = time.time()

    print(threading.current_thread(), threading.current_thread().name)
    print(f"fizz_buzz end：{num}\t所要時間：{end-bgn:.2f}秒\t累積時間：{end-bgn0:.2f}秒")
    return result_lst


# マルチスレッド
if __name__ == "__main__":
    bgn0 = time.time()
    num_lst = [i*10000000 for i in range(5, 0, -1)]
    for num in num_lst:
        th = Thread(target=fizz_buzz, args=(num, bgn0))
        th.start()
    print("start")

    # 処理中のスレッド一覧を返す
    for th in threading.enumerate():
        print(th, th.name)

    print("="*30)
