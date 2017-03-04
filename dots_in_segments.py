'''
В первой строке задано два целых числа 1≤n≤500001≤n≤50000 и 1≤m≤500001≤m≤50000 — количество отрезков и точек на прямой,
соответственно. Следующие nn строк содержат по два целых числа aiai и bibi (ai≤biai≤bi) — координаты концов отрезков.
 Последняя строка содержит mm целых чисел — координаты точек. Все координаты не превышают 108108 по модулю.
 Точка считается принадлежащей отрезку, если она находится внутри него или на границе. Для каждой точки в порядке
  появления во вводе выведите, скольким отрезкам она принадлежит.


Sample Input:
2 3
0 5
7 10
1 6 11
Sample Output:
1 0 0


Time Limit: 3 seconds
Memory Limit: 256 MB

'''


import sys

cache_dots = {}
cache_segm = {}
def partition_old(arr, l, r):
    x = arr[l]
    xs = 1
    j = l
    
    for i in range(l + 1, r + 1):
        if arr[i] < x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
            #        elif arr[i] == x:
            #            arr.insert()
        elif arr[i] == x:
            j += 1
            xs += 1
            arr.insert(0, arr.pop(i))
#    arr[l], arr[j] = arr[j], arr[l] # ставит 1й "по центру"
 #   arr.append(arr.pop(j)) # середниу перекинуть в конец
#    print('f ',arr)
#    print(arr[j:j+1])
    #arr[:len(xs)], arr[j:j+1] = arr[j:j+1], arr[:len(xs)]
    q = list(arr[j:j+1])
    arr.insert(j , )
    return j

def partition(arr, l ,r):
    '''Возвращает индекс последнего элемента, меньшего заданного
        и первый индекс элемента, больше заданного

    Разбивая на месте список на три части: меньше, равно и больше заданному
    числу
    '''
    mid = (l + r) // 2
    if arr[l] < arr[r] < arr[mid]:
        arr[l], arr[r] = arr[r], arr[l]
    elif arr[l] < arr[mid] < arr[l]:
        arr[l], arr[mid] = arr[mid], arr[l]
        
    x = arr[l]   
    xs = 1
    j = l
    for i in range(l + 1, r + 1):
        if arr[i] < x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
        elif arr[i] == x:
            j += 1
            xs += 1
            arr.insert(0, arr.pop(i))
    arr[:] = arr[xs:j+1] + arr[:xs] + arr[j+1:]
#    print(arr)
    return j - xs + 1, j + 1 #  : part[0]))) , [[[[part[1] : 
    
    
def quick_sort(arr, l, r):
    '''Сортирует список'''
    while l < r:
        m = partition(arr, l, r)
        if len(arr[:m[0]]) > len(arr[m[1]:]): # - +1
            quick_sort(arr, m[1], r)
            r = m[0] - 1
        else:
            quick_sort(arr, l, m[0] - 1)
            l = m[1]


count = 0


def belong_old(arr, dot):
    global count

    a = list(arr)
    mid_index = len(arr) // 2
    mid_el = arr[mid_index]
    #    if dot #in range(mid_el[1], mid_el[0] + 1):
    #    for tpl in arr:
    #        if dot in range(tpl[0], tpl[1] + 1):
    #            count += 1
    start = 0
    end = len(arr) - 1
    while True:
        if dot < mid_el[1]:
            start = mid_index
            break
        else:
            a = a[:mid_index]
            mid_index = len(a) // 2
            mid_el = arr[mid_index]

    a = list(arr)
    mid_index = len(arr) // 2
    mid_el = arr[mid_index]

    while True:
        if dot > mid_el[0]:
            end = mid_index
            break
        else:
            a = a[mid_index:]
            mid_index = len(a) // 2
            mid_el = arr[mid_index]

    for i, tpl in enumerate(arr[start: end + 1]):
        if tpl[1] <= dot <= tpl[0]:
            count += 1
        elif dot > tpl[0]:
            break
    res = count * 1
    count = 0
    return res


def belong(arr, elem, start):
    '''Находит, в какое количество отрезков входит точка

    Итерируясь по списку, начиная с первого вхождения

    '''
    if start == None: return 0
    counter = 0

    for tpl in arr[start:]:
 #       print('test tpl_2', tpl, elem, tpl[1] <= elem <= tpl[0] )
        if tpl[0] < elem: break
 #       print('test tpl', tpl, elem, tpl[1] <= elem <= tpl[0] )
        if tpl[1] <= elem <= tpl[0]:
            counter += 1 + cache_segm[tpl]
    return counter


def double(array, elem, l, r):
    '''Возвращает индекс первого отрезка, включающего в себя точку
    
    работает методом двоичного деления
    '''
    arr = list(array)
    m = (l + r) // 2

    while r - l > 2:

        if arr[m + 1][0] >= elem and\
            arr[m][0] < elem and\
            arr[m + 1][1] <= elem:
#            print('if')
            return m + 1
        elif arr[m][0] <= elem: # переход в левую часть
            r = m
            m = (l + r) // 2
  #          print('elif')
        else:#if arr[m][0] > elem:
            l = m
            m = (l + r) // 2
#            print('else')
 #   m = (l + r) // 2
    indx = l
 #   print('arr', array[l : r + 1])
    for tpl in array[l : r + 1]:
        if tpl[1] <= elem <= tpl[0]:
            return l
                        # возвращает индекс именно того элемента,
                        # который первый
                        # включает в себя точку
        l += 1
#    return  False

array = [(3, 1), (5, 3), (9, 6)]


def main():
    n, m = map(int, input().split())
    segments = []
    
    for _ in range(n):
        x, y = map(int, next(sys.stdin).split())
        if (y, x) not in cache_segm:
            segments.append((y, x))  ## REVERSE SIC!!!
            cache_segm[(y, x)] = 0 ## sic
        else:
            cache_segm[(y, x)] += 1
            n -= 1
        
    points = list(map(int, next(sys.stdin).split()))
    quick_sort(segments, 0, n - 1)
    
    for point in points:
        if point not in cache_dots:
            start = double(segments, point, 0, len(segments) - 1)
            quant = belong(segments, point, start) # кол-во вхождений
    #        cache_dots.update([(point, quant)])
            cache_dots[point] = quant
            print(quant, end=' ')
        else:
            print(cache_dots[point], end=' ')
        
    
    
def test():
    d = {}
    d[3] = 'three'
    d[(1,2)] = 'tpl'
    print(d)
    print((1,     2) in d)
if __name__ == '__main__':
    main()
#    a = [10, 8 , 12,3,10,11, 10, 14]
#    a = [10, 10, 10, 8, 3, 12, 11, 14]

 #   print(a)
 #   print(partition(a,0,7))
 #   print(a)
    
