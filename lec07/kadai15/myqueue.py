class PriorityQueue:
    def __init__(self):
        self._lst = []

    def enqueue(self, item):
        self._lst.append(item)

    def dequeue(self):
        if len(self._lst) == 0:
            return None
        return self._lst.pop(0)
