'''Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его
соседей. Для элементов списка, являющихся крайними, одним из соседей считается
элемент, находящий на противоположном конце этого списка. Например, если на
вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7"
(без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными
пробелом.'''
a = input().split()
b = []
if len(a) > 1:
    for i, num in enumerate(a):
        try:
            b.append(int(a[i-1]) + int(a[i+1]))
        except IndexError:
            b.append(int(a[i-1]) + int(a[0]))

    for s in b:
        print(s, end=' ')
else:
    print(a[0])
