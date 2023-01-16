def greeting(greet):
    return f"{greet} world!"

print( greeting("1. hello") )


# 変数に代入することができる
aisatsu = greeting
print( aisatsu("2. hello") )


# コンテナの要素とすることができる
funcs = [greeting, str.upper, str.capitalize]
for f in funcs:
    print( f("3. hello") )


# 他の関数に引数として渡すことができる
def hoge(f, *args):
    s = []
    for arg in args:
        s.append( f(arg.capitalize()) )
    return " and ".join(s)

print( hoge(greeting, "hello", "good morning", "goodbye") )


# 関数内関数
def make_greeting(time):
    def inner1(text):
        return f"Good morning {text}!"

    def inner2(text):
        return f"Hello {text}!"

    def inner3(text):
        return f"Good evening {text}!"

    if  5 < time < 10:
        return inner1
    if 10 < time < 17:
        return inner2
    else:
        return inner3

print( make_greeting(6)("world") )
print( make_greeting(16)("world") )
print( make_greeting(23)("world") )