import collections
import random


class GameManager:
    cnt = 0

    def __init__(self, title, num):
        self.title = title
        self.num = num
        self.score_history = collections.defaultdict(int)

    def __enter__(self):
        print(f"=== ゲーム「{self.title}」開始 ===")
        print(f"{self.num}回チャレンジします")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("=== ゲーム終了 ===")
        print(f"スコア履歴：{self.score_history}")
        if exc_value is None:
            print("正常終了")
        else:
            print(f"{self.cnt}回目プレイ中に例外発生", exc_type, exc_value)

    def play(self):
        __class__.cnt += 1
        print(f" = {__class__.cnt}回目：プレイ開始")
        score = random.randint(-3, 5)
        if score < 0:
            raise ValueError(f"スコア異常 {score}")
        print(f" = {__class__.cnt}回目：プレイ終了")
        self.score_history[score] += 1


if __name__ == "__main__":
    with GameManager("逃げろ！こうかとん", 5) as game:
        for _ in range(game.num):
            game.play()
