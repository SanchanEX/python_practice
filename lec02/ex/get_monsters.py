from pokemon import Pikachu
from copy import copy, deepcopy

print('=============================')
Pikachu.get_num()   # イニシャライザを起動させる前の数

print('=============================')
monsters = [Pikachu(f"野生のピカチュウその{i+1}") for i in range(2)]

monsters.append(monsters[0])
monsters.append(copy(monsters[0]))
monsters.append(deepcopy(monsters[0]))
monsters[0].types.append("ひこう")
monsters[1].types.append("ドラゴン")

for mon in monsters:
    mon.appear()

# IDチェック
for mon in monsters:
    print(id(mon), id(mon.name), id(mon.types))
# 同一性チェック，等価性チェック
for mon in monsters:
    print(monsters[0] is mon, monsters[0] == mon)

for mon in monsters:
    print(mon.name, mon.types)

print('=============================')
Pikachu.get_num()   # イニシャライザを起動させた後の数

print('=============================')
print(f"Lv.{monsters[0].level}")
monsters[0].level = -10     # 直接アクセスは不正な値も設定できてしまう -> propertyによるアクセスを用いて回避
print(f"Lv.{monsters[0].level}")

print('=============================')
print(vars(monsters[0]))
monsters[0]._Pikachu__level = -10   # _クラス名__属性名にマングリング
monsters[0].__level = -20           # メンバの追加
print(vars(monsters[0]))

print('=============================')
print(monsters)
print(monsters[0])

print('=============================')
