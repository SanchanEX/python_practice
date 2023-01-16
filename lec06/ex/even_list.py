class EvenList(list):
    def __setitem__(self, idx, value: int):
        if value%2 != 0:
            raise ValueError("奇数は設定できません")
        super().__setitem__(idx, value)

    def append(self, value):
        if value%2 != 0:
            raise ValueError(f"奇数は設定できません：{value}")
        super().append(value)

if __name__ == "__main__":
    eve_lst = EvenList()
    for i in range(10):
        try:
            eve_lst.append(i)
        except Exception as e:
            print(e)
    print(len(eve_lst), eve_lst)
