'''
По данным n

отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100
отрезков. Каждая из последующих n строк содержит по два числа
0≤l≤r≤109, задающих начало и конец отрезка. Выведите оптимальное
число m точек и сами m точек. Если таких множеств точек несколько,
выведите любое из них.
'''

n = int(input())
v = []
points = []
for i in range(n):
    x, y = input().split()

    v.append(tuple([int(x), int(y)]))
dots = set()
# сортируем по концам отрезков, потому что конец
#считается в задаче "оптимальной" точкой и конец как раз и определяет
#возможность пересечения
v = sorted(v, key=lambda x: x[1])
"""
всегда берем эту точку, потому что в отсортированном по концу
отрезка массиве всегда есть хотя бы один больше, либо отрезки
не пересекаются вообще
"""
r = v[0][1]

dots.add(r)
for pair in v:
    # если последняя точка не в отрезке
    # если конец не находится в следующем отрезке
    # если не пересекаются
    if not (r >= pair[0] and r <= pair[1]):
        r = pair[1] # надежная точка заменяется на конец следующего
        dots.add(r)

print (len(dots))
print (' '.join([str(_) for _ in dots]))

           


