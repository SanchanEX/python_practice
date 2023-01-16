from dataclasses import dataclass

"""
優先度付きキュー
"""


@dataclass
class Monster:
    level: int
    title: str

    def __repr__(self):
        return f"{self.title}(Lv.{self.level})"


class PriorityQueue:
    def __init__(self):
        self._lst = []

    # 要素を追加する関数
    def enqueue(self, item):
        self._lst.append(item)
        # enqueueするたびに内部リストを優先度で降順ソート
        self._lst.sort(key=lambda item: item.level, reverse=True)

    # 要素を抽出する関数
    def dequeue(self):
        if len(self._lst) == 0:
            return None
        return self._lst.pop(0)

    def __repr__(self):
        return "　".join([f"{i}: {mon}" for i, mon in enumerate(self._lst, 1)])


if __name__ == "__main__":
    # 優先度が高い要素が前にくるようにenqueueされる
    que = PriorityQueue()

    que.enqueue(Monster(25, "ピカチュウ"))
    que.enqueue(Monster(60, "カイリュウ"))
    que.enqueue(Monster(40, "ヤドラン"))
    que.enqueue(Monster(20, "ピジョン"))
    print(que)
    print('')

    for i in range(2):
        print(que.dequeue())

    que.enqueue(Monster(15, "コダック"))
    que.enqueue(Monster(10, "コラッタ"))
    que.enqueue(Monster(30, "ズバット"))
    que.enqueue(Monster(45, "ギャロップ"))
    print('')
    print(que)
