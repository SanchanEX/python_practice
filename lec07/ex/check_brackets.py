from collections import deque


class BracketChecker:
    left = {"(": 0, "{": 1, "[": 2, "<": 3}
    right = {")": 0, "}": 1, "]": 2, ">": 3}

    def __init__(self, sentence: str):
        self.sentence = sentence

    def check(self):
        stk = deque()   # スタックを空にする
        for s in self.sentence:  # 文字列を順に取得
            if s in __class__.left:  # 左が現れたらスタックにpushする
                stk.append(s)
            if s in __class__.right:    # 右が現れたら
                try:    # 空でなければpopする
                    item = stk.pop()
                    if __class__.left[item] == __class__.right[s]:
                        print(f"一致しました：{item} {s}")
                except Exception as e:  # 空ならエラー
                    print(f"一致する左括弧がありません{e}")


if __name__ == "__main__":
    bc = BracketChecker("(())(())((()())))()))()")
    bc.check()
    print("-"*30)
    bc = BracketChecker(
        "if ((key in self and self[key] != value) or (key not in self)):")
    bc.check()
    print("-"*30)
    bc = BracketChecker(
        "\delta(d) &=& \frac{1}{\gamma(d)-1}\sum_{\substack{j = 1 \\ c_j, c_{j+1} \in \Gamma(d)}}^{\gamma(d)-1} {c_{j+1}.time - c_j.time}")
    bc.check()
