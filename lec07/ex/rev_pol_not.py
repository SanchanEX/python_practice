from collections import deque


class RevPolishNotation:
    operators = {"+", "-", "*", "/"}

    def __init__(self, expression: str):
        """
        逆ポーランド記法の数式文字列をスペースで分割したリストを構築
        """
        self.items: list = expression.split()

    def calculate(self):
        # print("="*30)
        print(self.items)
        stk = deque()
        for s in self.items:
            try:
                float(s)
                stk.append(s)
                # print(stk)
            except Exception as e:
                if s in __class__.operators:
                    right = stk.pop()
                    # print(right)
                    left = stk.pop()
                    # print(left)
                    expression = left + s + right
                    result = eval(expression)
                    # print(result)
                    stk.append(str(result))
                    # print(stk)


if __name__ == "__main__":
    rpn = RevPolishNotation("1 2 + 3 4 + *")
    rpn.calculate()
    # print(rpn)
    print("-"*30)
    rpn = RevPolishNotation("5 4 3 + *")
    rpn.calculate()
    print("-"*30)
    rpn = RevPolishNotation("3 4 + 1 2 - *")
    rpn.calculate()
