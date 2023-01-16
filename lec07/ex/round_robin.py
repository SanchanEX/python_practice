from dataclasses import dataclass
from random import randint
from collections import deque


@dataclass
class Process:
    title: str = None
    duration: int = 0 # このプロセスの所要時間[秒]

class RoundRobin:
    def __init__(self, quantum):
        self.quantum = quantum
        self.total = 0
    
    def schedule(self, processes):
        que = deque(processes)
        print(que)
        while True:
            try:
                p = que.popleft()
                self.total += p.duration
                p.duration -= self.quantum
                if p.duration > 0:
                    que.append(p)
                    print(f"未完：{p}")
                else:
                    print(f"完了：{p}")
            except Exception as e:
                break
        print(f"全所要時間：{self.total}")

if __name__ == "__main__":
    rr = RoundRobin(5) # 1回の処理は5秒のみ
    rr.schedule([Process(f"プロセス{i+1}", randint(1, 15)) for i in range(10)])
        