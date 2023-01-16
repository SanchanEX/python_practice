import libqueue
import myqueue
from time import process_time
import random


class QueueTimeMeasurement:
    def __init__(self, que):
        self.que = que
        self.begin = 0  # 開始時間
        self.end = 0    # 終了時間

    def exec(self, *num_enqueue):
        self.begin = process_time()
        # num_enqueueが指定されていなければ10000に設定
        if not num_enqueue:
            num_enqueue = (10000,)
        # print(num_enqueue[0])
        i = 0
        for _ in range(num_enqueue[0]):
            i += 1
            self.que.enqueue(random.random())
            # myqueue.PriorityQueue.enqueue(self.que, random.random())
            if i % 10 == 0:
                self.que.dequeue()
        self.end = process_time()
        self.result = self.end - self.begin

    def get_duration(self):
        return format(self.result, '.6f')


if __name__ == "__main__":
    libque = QueueTimeMeasurement(libqueue.PriorityQueue)
    libque.exec(100000)
    print(f"libque: {libque.get_duration()}")

    myque = QueueTimeMeasurement(myqueue.PriorityQueue)
    myque.exec(100000)
    print(f"myque: {myque.get_duration()}")
