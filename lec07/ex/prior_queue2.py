import heapq

que = []
heapq.heappush(que, (25, "ピカチュウ"))
heapq.heappush(que, (60, "カイリュウ"))
heapq.heappush(que, (40, "ヤドラン"))
heapq.heappush(que, (20, "ピジョン"))

for i in range(5):
    print(heapq.heappop(que))
