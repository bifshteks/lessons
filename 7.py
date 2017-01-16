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

n = 9
# n = int(input())

a = [i for i in range(1, n*n + 1)]    # [1, 2, ... , 9]
b = [['' for c in range(n)] for c in range(n)]

'''[['','','']
    ['','','']
    ['','','']]
'''

def fill_line(line, start, backwards=False):
    i = start
    r = range(n)
    
    if backwards:
        r = reversed(r)
    for j in r: # идем по всей строке и ищем пустоты.
        
        
        end = j
        if not b[line][j]: # если не заполнена, то надо заполнить
            b[line][j] = i
            i+=1
            
        # проверяем что не вышли за границы и если не вышли,
        # то проверям что не заполнен след (или пред. если идем в 
        #обратном порядке) элемент. 
        # Если заполнен, то прерываемся.


        if backwards:
            if '' not in b[line] and b[line][j-1]: break
        else:
            if '' not in b[line] and (b[line][j+1] if j != n - 1 else True): break
    
    return i, end



def fill_col(col, start, backwards=False):
    i = start
    r = range(n)
    
    
    if backwards:
        r = reversed(r)
    for j in r:
        columns = [b[w][col] for  w in range(n)]
        
        if backwards:
            if '' not in columns and b[j-1][col]: break
        else:
            if '' not in columns and (b[j+1][col] if j != n-1 else True): break

        end = j
        if not b[j][col]:
            b[j][col] = i
            i+=1
    
    return i, end



z = 1
r = 0


for c in range(1, n+1):
    if c == n:
            z, r = fill_line(r, z)

    else:
        
        if c % 2 == 1: 
            z, r = fill_line(r, z)
            z, r = fill_col(r, z)
        else:
            z, r = fill_line(r, z, True)
            z, r = fill_col(r, z, True)

    


max_len = len(str(max(range(1,n*n + 1))))
#print('max_len = ', max_len)
for q in b:
    for y, p in enumerate(q):
        while True:
            if len(str(q[y])) < max_len:
                q[y] = str(q[y]) + ' '
            else:
                q[y] = str(q[y])
                break

for l in b:
    print(l)
'''       
for l in b:
    [print(num, end=' ') for num in l[:-1]]
    print(l[-1])

'''

