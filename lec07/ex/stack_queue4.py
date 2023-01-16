from dataclasses import dataclass
from collections import deque

@dataclass
class Monster:
    title: str

    def __repr__(self):
        return self.title


if __name__ == "__main__":
    stk = deque()
    stk.append(Monster("ピカチュウ"))
    stk.append(Monster("カイリュウ"))
    stk.append(Monster("ヤドラン"))
    stk.append(Monster("ピジョン"))
    print(stk)

    print("-"*10)
    for i in range(5):
        print(stk.pop())
    print("################################")
    que = deque()
    que.append(Monster("ピカチュウ"))
    que.append(Monster("カイリュウ"))
    que.append(Monster("ヤドラン"))
    que.append(Monster("ピジョン"))
    print(que)

    print("-"*10)
    for i in range(5):
        print(que.popleft())
    