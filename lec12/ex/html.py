class Monster:
    def __init__(self, title):
        self.title = title


# def li_decorator(func):
#     def _func(t):
#         s1 = "<li>"
#         s2 = func(t)
#         s3 = "</li>"
#         return s1+s2+s3+"\n"
#     return _func


# def ul_decorator(func):
#     def _func(t):
#         s1 = "<ul>"
#         s2 = func(t)
#         s3 = "</ul>"
#         return s1+s2+s3+"\n"
#     return _func

def tag_decorator(tag):
    def _decorator(func):
        def _func(t):
            s1 = "<"+tag+">"
            s2 = func(t)
            s3 = "</"+tag+">"
            return s1+s2+s3+"\n"
        return _func
    return _decorator


# @li_decorator
@tag_decorator("li")
def get_title(mon):
    return mon.title


# @ul_decorator
@tag_decorator("ul")
def concat_strs(mon_lst):
    s = []
    for item in mon_lst:
        s.append(get_title(item))
    return "".join(s)


if __name__ == "__main__":
    monsters = [
        Monster("イーブイ"),
        Monster("シャワーズ"),
        Monster("サンダース"),
        Monster("ブースター"),
        Monster("エーフィ"),
        Monster("ブラッキー"),
        Monster("リーフィア"),
        Monster("グレイシア"),
        Monster("ニンフィア"),
    ]

    print(concat_strs(monsters))
