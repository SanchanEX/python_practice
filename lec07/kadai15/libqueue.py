import queue


class PriorityQueue(queue.PriorityQueue()):
    def enqueue(self):
        return super().put()

    def dequeue(self):
        return super().get()
