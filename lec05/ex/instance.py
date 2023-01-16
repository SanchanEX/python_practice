a = 243 # 整数
print(type(a))

a = 172.5 # 実数
print(type(a))

a = [1, 2, 0, 1] # リスト
print(type(a))

a = "fsm" # 文字列
print(type(a))

a = int # 型
print(type(a))

a = lambda : 27 # ラムダ式
print(type(a))

def f(): # 関数
    return 27
a = f
print(type(a))

class Monster: # 自作クラス
    def __init__(self, title):
        self.title = title

a = Monster
print(type(a)) # 自作クラス
print(type(a.__init__)) # 自作クラスのインスタンスメソッド（クラス経由）

a = Monster("ピカチュウ") # 自作クラスのインスタンス
print(type(a))
print(type(a.__init__)) # 自作クラスのインスタンスメソッド（インスタンス経由）