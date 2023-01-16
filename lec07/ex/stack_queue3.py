from dataclasses import dataclass
from queue import LifoQueue, Queue

@dataclass
class Monster:
    title: str

    def __repr__(self):
        return self.title


if __name__ == "__main__":
    stk = LifoQueue()
    stk.put(Monster("ピカチュウ"))
    stk.put(Monster("カイリュウ"))
    stk.put(Monster("ヤドラン"))
    stk.put(Monster("ピジョン"))
    print(stk)

    print("-"*10)
    for i in range(5):
        print(stk.get())
    print("################################")
    que = Queue()
    que.put(Monster("ピカチュウ"))
    que.put(Monster("カイリュウ"))
    que.put(Monster("ヤドラン"))
    que.put(Monster("ピジョン"))
    print(que)

    print("-"*10)
    for i in range(5):
        print(que.get())
    