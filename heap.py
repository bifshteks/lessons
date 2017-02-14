def siftup(el, lst):
    '''По возможности просеевает число вверх'''
    lst.append(el)
    index_el = len(lst) - 1
    index_father = index_el // 2
#    father = lst[index_father]
#    el = lst[index_el]
    
    while True:
        if lst[index_father] > lst[index_el]: # if not correct
            new_index_el, index_father = index_father, index_el
            lst[new_index_el], lst[index_el] = lst[index_el], lst[new_index_el]
            index_new_father = new_index_el // 2
            index_father = index_new_father
        else: 
#            print(lst)
            return index_el

        
def sift_down(index_el, lst):
    '''По возможности просеевает число вниз'''
    el = lst[index_el]
    index_ch_1 = index_el * 2
    index_ch_2 = index_el*2 + 1
#    child_1 = lst[index_ch_1]
#    child_2 = lst[index_ch_2]
    while True:
        if index_ch_1 <= len(lst) - 1 and \
           index_ch_2 <= len(lst) - 1 and \
           child_1 < el and child_2 < el:
            child_1 = lst[index_ch_1]
            child_2 = lst[index_ch_2]
            if min(child_1, child_2) == child_1:
                index_el, index_ch_1  = index_el * 2, index_el
                lst[index_el], lst[index_ch_1] = el, lst[index_el]
            else:
                index_el, index_ch_2  = index_el * 2 + 1, index_el
                lst[index_el], lst[index_ch_2] = el, lst[index_el]
       # elif index_ch_1 <= len(lst) - 1 and index_ch_2 <= len(lst) - 1 and child_1 < el and child_2 >= el :
        elif index_ch_1 <= len(lst) - 1  and child_1 < el :
            child_1 = lst[index_ch_1]
            index_el, index_ch_1  = index_el * 2, index_el
            lst[index_el], lst[index_ch_1] = el, lst[index_el]
#        
        elif index_ch_2 <= len(lst) - 1 and child_2 < el :
            child_2 = lst[index_ch_2]
            index_el, index_ch_2  = index_el * 2 + 1, index_el
            lst[index_el], lst[index_ch_2] = el, lst[index_el]
        else: break

        
def find_max(lst):
    '''возвращает наибольшее число'''
    len_list = len(lst) 
    power_num = 0
    while True:
        if 2 ** (power_num + 1) < len_list:
            power_num += 1
#    while 2 ** (power_num + 1) < len_list:
#        power_num += 1
        else: break
    maximum = max(lst[2 ** power_num - 1:])
    res = 0
    for i, n in enumerate(lst[2 ** power_num:]):
        if n == maximum:
            res = i
#    index = res + 2 ** power_num - 1 if len_list > 0 else res + 2 ** power_num 
    index = res + 2 ** power_num if len_list > 0 else res + 2 ** power_num - 1
    return lst.pop(index)


def insert(x):
    '''Добавляет число в кучу'''
    if len(prior) > 3:
            sift_down(siftup(x, prior),prior)
    else:
        siftup(x, prior)
        
       
n_com = int(input())
prior = [float('-inf')]
max_value = 0

for _ in range(n_com):
    comm = input()
    if comm.startswith('Insert'):
        number = int(comm.split()[1])
     #       prior.append(number)
        if len(prior) > 3:
            sift_down(siftup(number, prior),prior)
        else:
            siftup(number, prior)
 #       if number > max_value:
 #           max_value = number
    else:
        print(find_max(prior[1:]))
#print(prior)
