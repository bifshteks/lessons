n = int(input())
a = []
points = []
for i in range(n):
    x = [int(k) for k in input().split()]
a.append(list(x))
a = sorted(a, key=lambda tpl: tpl[0])
end = len(a)
i = 1
print('a = ', a)
def foo(lst, i):
    if lst[i][1] >= lst[i+1][0] and a[i-1][1] >= a[i+1][0]:
        v = 1
        while True:
            if a[i-1][1] <= a[i+v][1]:
                break
            v += 1
        for j in range(v):
            pass
    elif lst[i][1] >= lst[i+1][0]:
        return [lst[i+1][0],lst[i][1]]


while True:
    if len(a) > 2:
        if a[i-1][1] >= a[i][0] and a[i-1][1] >= a[i+1][0]: # if cover both
            if a[i+1][0] > a[i][1]:
                points.append(a[i][1])
                del a[1], a[0]
            else:
                a[i][1] = a[i-1][1]
                del a[0]
        else:
            points.append(a[i][0])
            del a[0]
        print('a = ', a)
        print('points = ', points)
    elif len(a) == 2:
        if a[i-1][1] >= a[i][0]:
            a[i][1] = a[i-1][1]
            del a[0]

        else:
            points.append(a[i][0])
            del a[0]
        print('a = ', a)
        print('points = ', points)
    else:
        points.append(set(a[0]).pop())
        print('a[0] = ', a[0])
        break
print('dlina =',len(points))
[print(' Tochka =',point, end=' ') for point in points]
