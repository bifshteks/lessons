'''Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке,
как показано в примере (здесь n=5):

Sample Input:

5

Sample Output:

1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''



n = int(input())
a = [i for i in range(1, n*n + 1)]
b = [['' for c in range(n)] for c in range(n)]

for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][j] == '':
            b[i][j] = a[0]
            del a[0]
print('a =', a)
print('b = ', b)
                
        




