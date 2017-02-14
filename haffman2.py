'''
По данной непустой строке s длины не более 104, состоящей из строчных
букв латинского алфавита, постройте оптимальный беспрефиксный код.
В первой строке выведите количество различных букв k, встречающихся
в строке, и размер получившейся закодированной строки. В следующих k
строках запишите коды букв в формате "letter: code". В последней строке
выведите закодированную строку.
'''
def doub_min(lst):
    '''возвращает два минимальных числа из списка

    в виде [
            сумма_их_приоритетов,
            [все_значения_из_обоих],
            контейнер_значений
            ]
            '''
    copy = lst[:]
    m = min(copy,key=lambda x: x[0])
    del copy[copy.index(m)]
    m_2 = min(copy,key=lambda x: x[0])

    try:
        c = m[2][:]
        del c[c.index('stop')]
        r = [x for x in c]
    except:
        r = [x for x in m[2]]
    try:
        v = m_2[2][:]
        del v[v.index('stop')]
        d = [x for x in v]
    except:
        d = [x for x in m_2[2]]
    r.append('stop')
    r.extend(d)
    all_in =(r)
    
    return [m[0] + m_2[0], [m[1:], m_2[1:]], all_in]
#          prior            symb  symb      tree

def find_way(el, branch):
    global way
    

    try:
        x = branch[-1][:branch[-1].index('stop')]
        y = branch[-1][branch[-1].index('stop') + 1:]
    except:
        x = []
        y = []

    if type(branch[0]) == str:
        res = way[:] if len(way) > 0 else '0'
        way = ''
        return res
    
    elif el in x:# еслив собирателе слева
        way += '0'

        return find_way(el, branch[-2][0])
    elif el in y:# если в собирателе справа
        way += '1'

        return find_way(el, branch[-2][1])


s = input()
tree = {}
prior = []
for el in set(s):
    prior.append([s.count(el), el, [el]])

prior.sort(key=lambda x: x[0])

while len(prior) > 1:
    qwe = doub_min(prior)
    
    del prior[0]
    del prior[0]
    prior.insert(0, qwe)
    prior.sort(key=lambda x: x[0])

    

prior = prior[0][1:]


way = ''
coding = {}
for symb in set(s):
    coding[symb] = find_way(symb, prior)

result_string = ''
for symb in s:
    result_string += coding[symb]
    
print(len(set(s)), len(result_string))
for k, v in coding.items():
    print(k, ': ', v, sep='')
print(result_string)
