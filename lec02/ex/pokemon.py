class Pikachu:      # ピカチュウの設計書
    num = 0         # クラス変数の初期化
    title = "ピカチュウ"  # クラス変数の初期化

    def __init__(self, name):
        self.name = name    # nameのインスタンス変数
        self.types = ["でんき"]
        self.level = 5      # levelのデフォルト値

        Pikachu.num += 1    # クラス変数へのアクセス

    def appear(self):       # 出現のインスタンスメソッド
        print(f"{self.name}が現れた")

    @classmethod            # クラスメソッドの定義
    def get_num(cls):
        print(f"{cls.num}匹の{cls.title}がいる")

    @property
    def level(self):
        return self.__level  # マングリング

    @level.setter
    def level(self, val):
        if val < 0:
            print("不正な値のため，設定を中止します．")
        else:
            self.__level = val  # マングリング

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __eq__(self, other):
        return self.title == other.title
