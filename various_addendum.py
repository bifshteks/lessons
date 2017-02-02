'''
По данному числу 1≤n≤109 найдите максимальное число k,
для которого n можно представить как сумму k различных натуральных
слагаемых. Выведите в первой строке число k, во второй — k слагаемых.
'''
import sys


sys.setrecursionlimit(50000)
n = int(input())
q = n*1
#a = [i for i in range(1, n+1)] # [1, 2, 3, 4]
res = []

j = 1
count = 0
def my(n):
    '''Return the next valid number 

    '''
    global count
    global j
    count += 1
    if  n - j == 0 or n - j >= j+1:  
        res.append(j)
        num = j*1
        j += 1
        return num
    else:
        j += 1
        return my(n)  


i = 0
while True:
#for i in range(1000):
    if n != 0:
        n -= my(n)
    else:
        break
    i += 1

print(len(res))
[print(x, end=' ') for x in res]
