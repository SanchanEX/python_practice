title = "イーブイ"
print(title[2])
print(title.__getitem__(2))
print(title, dir(title)) # strオブジェクトの属性一覧
title_itr = iter(title)  # iterableからイテレータを作成
print(title_itr, dir(title_itr))

print(next(title_itr)) # 1回目
print(next(title_itr)) # 2回目
print(next(title_itr)) # 3回目
print(next(title_itr)) # 4回目
#print(next(title_itr)) # 5回目

evols = {"シャワーズ", "サンダース", "ブースター", "エーフィ", "ブラッキー", "リーフィア", "グレイシア", "ニンフィア"}
print(evols, dir(evols)) # 集合オブジェクトの属性一覧
evols_itr = iter(evols)  # iterableからイテレータを
print(evols_itr, dir(evols_itr))

print(next(evols_itr)) # 1回目
print(next(evols_itr)) # 2回目
print(next(evols_itr)) # 3回目
print(next(evols_itr)) # 4回目


