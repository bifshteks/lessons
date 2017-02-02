'''
Первая строка содержит количество предметов 1≤n≤103 и вместимость рюкзака
0≤W≤2⋅106. Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅106 и объём
0<wi≤2⋅106 предмета (n, W, ci, wi — целые числа). Выведите максимальную
стоимость частей предметов (от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный
рюкзак, с точностью не менее трёх знаков после запятой.
'''
import numpy as np

'''
Тест прошел, но на моем ноутбуке атрибута .float128 не существует.
На сколько я понял это зависит от битности python'а и ноута и в моем случае
официального работающего релиза еще не вышло
'''
n, w = map(int, input().split())
items = {}
things = []
bag = [w]
for i in range(n):
    coast, weight = map(int, input().split())
    things.append(tuple([coast, weight]))

things = sorted(things, key=lambda tpl: tpl[0] / tpl[1], reverse= True)

for both in things:
    if both[1] <= bag[0]:
        bag.append(both[0])
        bag[0] -= both[1]
    else: 
        bag.append(np.float128(both[0]) / np.float128(both[1]) *\
                                           np.float128(bag[0]))
        break
        print(np.float128(both[0]) / np.float128(both[1]) *\
                                      np.float128(bag[0]))
del bag[0]
print(round(sum(bag), 3))
