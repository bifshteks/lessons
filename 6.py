'''Напишите программу, на вход которой подаётся прямоугольная матрица в
виде последовательности строк, заканчивающихся строкой, содержащей только
строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент
в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j),
(i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится
с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по
соответствующему направлению.
'''

a = []
while True:
    n = input().split()
    if n != ['end']:
        n = [int(i) for i in n]
        a.append(n)
    else:
        break
    

def get_col_index(i, j):
    """принимает индекс столбца слева или справа. если элемент находится справа у края, возвращает 0.
    если меньше нуля - самый правый
    если индекс где-то в середине его и возвращает"""
    
    if j >= len(a[i]):   
        r = 0
    elif j < 0:   
        r = len(a[i])-1
    else:
        r = j
    return r


def get_row_index(i):
    if i >= len(a):
        r =  0
    elif i < 0:
        r = len(a)-1
    else:
        r =  i
    return r


r = [[] for i in range(len(a))]
for i, b in enumerate(a):
    for j, l in enumerate(b):
        x = a[get_row_index(i-1)][j] + a[get_row_index(i+1)][j] +\
            a[i][get_col_index(i, j-1)] + a[i][get_col_index(i, j+1)]
        r[i].append(x)

for i, line in enumerate(r):
    for j, el in enumerate(r[i]):
        if j != len(r[i]) - 1:
            print(el, end=' ')
        else:
            print(el)
