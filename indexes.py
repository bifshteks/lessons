'''
Первая строка содержит число 1≤n≤105, вторая — массив A[1…n],
содержащий натуральные числа, не превосходящие 109. Необходимо
посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
(Такая пара элементов называется инверсией массива. Количество инверсий в
массиве является в некотором смысле его мерой неупорядоченности: например,
в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве,
упорядоченном по убыванию, инверсию образуют каждые два элемента.)
'''

import sys


count = 0
def merge(arr1, arr2):
    '''Объеденяет и два массива в один отсортированный'''
    global count

    result_arr = []
    while len(arr1) > 0 and len(arr2) > 0:

        if arr1[0] > arr2[0]:
            count += len(arr1)
            minim = arr2.pop(0)
            result_arr.append(minim)
        else:

            minim = arr1.pop(0)
            result_arr.append(minim)
    else:
        result_arr.extend(arr1 if arr1 else arr2)

    return result_arr


def merge_sort(arr):
    '''Соритрует массив'''
    global count
    if len(arr) > 2:
        m = len(arr) // 2
        foo = arr[:m]
        
        return merge(merge_sort(foo), merge_sort(arr[m:]))
    else:
        if arr[0] > arr[-1]: count += 1
        x = sorted(arr)
        
        return x

    
def main():
    global count
    reader = (list(map(int, line.split())) for line in sys.stdin)
    len_arr = next(reader)[0]
    arr = next(reader)
    merge_sort(arr)
    print(count)

if __name__ == '__main__':
    main()
    
