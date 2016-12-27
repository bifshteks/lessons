n = 3    #int(input())
'''table = {}
a = []
for p in range(n):
    game = input().split(';')

    a.extend([{game[0]: int(game[1]), game[2]: int(game[3]) }])

    if game[0] not in table:
        table.update([(game[0], [int(game[1])])])
    elif game[0] in table:
        table[game[0]].append(int(game[1]))

    if game[2] not in table:
        table.update([(game[2], [int(game[3])])])
    elif game[2] in table:
        table[game[2]].append(int(game[3]))


'''
def dif_item(d, key):
    lst = list(d.items())
    print('lst =====', lst)
    if lst[0][0] == d[key]:
        return lst[1][1]
    else:
        return lst[0][1]
#        table.add((game[0], int(game[1])),(game[2], int(game[3])))
#inp = [ {a: 1, b: 2}, {c: 1, b: 3} , ...]
table = {'Зенит': [3, 2], 'Спартак': [1, 1], 'ЦСКА': [1, 0]}
a = [ {'Зенит': 3,'Спартак': 1}, {'Спартак': 1, 'ЦСКА': 1}, {'ЦСКА': 0,'Зенит': 2}]

res = {}
for com, nums in table.items():
    win = 0
    lose = 0
    pat = 0
    for d in a:
        if com in d:
            if d[com] > dif_item(d, com):
                win += 1

            elif d[com] < dif_item(d, com):
                lose += 1
                
            else:
                pat += 1
        print('coma = ', com)
        print('win =',win, 'lose =',lose, 'pat =',pat)
    
    list_com = [( com, [ len(nums), win, pat, lose,  win*3 + pat ])]
    res.update(list_com)

print(res)
print( dif_item(a[0], 'Зенит'))
