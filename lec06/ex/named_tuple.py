from collections import namedtuple

### まずはふつうのtuple
fushi = ("フシギダネ", 25, "くさ どく")
print(fushi) # tupleのprint
print(fushi[0]) # tupleの要素にアクセス
tit, lev, typ = fushi # tupleのアンパック
print(tit, lev, typ)
for item in fushi: # tupleはiterable
    print(item)
#fushi[0] = "フシギソウ" # tupleはimmutable


print("-"*20)


### ここからnamedtuple
Monster = namedtuple("Monster", ["title", "level", "type_"])
fushi = Monster("フシギダネ", 25, "くさ どく")
print(fushi) # namedtupleのprint
print(fushi.title) # namedtupleのフィールドにアクセス
tit, lev, typ = fushi # namedtupleのアンパック
print(tit, lev, typ)
for item in fushi: # namedtupleはtupleと同じくiterable
    print(item)
#fushi.title = "フシギソウ" # namedtupleはtupleと同じくimmutable