from queue import PriorityQueue

que = PriorityQueue()
que.put((25, "ピカチュウ"))
que.put((60, "カイリュウ"))
que.put((40, "ヤドラン"))
que.put((20, "ピジョン"))
for i in range(5):
    print(que.get())
