'''
По данному числу 1≤n≤109 найдите максимальное число k,
для которого n можно представить как сумму k различных натуральных
слагаемых. Выведите в первой строке число k, во второй — k слагаемых.
'''
k = int(input())
i = 1
res = []
while True:
    if k - i <= i:
        res.append(k)
        break
    else:
        res.append(i)
        k -= i
        i += 1
print(len(res))
[print(x,end=' ') for x in res]
