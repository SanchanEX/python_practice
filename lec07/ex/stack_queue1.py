from dataclasses import dataclass


@dataclass
class Monster:
    title: str

    def __repr__(self):
        return self.title


class Stack:
    def __init__(self):
        self._lst = []  # インスタンス化

    def push(self, item):
        self._lst.append(item)  # 内部リストにappend

    def pop(self):
        if len(self._lst) == 0:
            return None
        return self._lst.pop()

    def __repr__(self):
        return "\n".join([f"{len(self._lst)-i+1}: {mon}" for i, mon in enumerate(self._lst[::-1], 1)])


class Queue:
    def __init__(self):
        self._lst = []

    def enqueue(self, item):
        self._lst.append(item)

    def dequeue(self):
        if len(self._lst) == 0:
            return None
        return self._lst.pop(0)

    def __repr__(self):
        return "　".join([f"{i}: {mon}" for i, mon in enumerate(self._lst, 1)])


if __name__ == "__main__":
    stk = Stack()
    stk.push(Monster("ピカチュウ"))
    stk.push(Monster("カイリュウ"))
    stk.push(Monster("ヤドラン"))
    stk.push(Monster("ピジョン"))
    print(stk)
    # print(len(stk))

    print("-"*10)
    for i in range(5):
        print(stk.pop())
    print("################################")
    que = Queue()
    que.enqueue(Monster("ピカチュウ"))
    que.enqueue(Monster("カイリュウ"))
    que.enqueue(Monster("ヤドラン"))
    que.enqueue(Monster("ピジョン"))
    print(que)
    # print(len(que))

    print("-"*10)
    for i in range(5):
        print(que.dequeue())
