import random


def rec(n):
    def foo(n, lst, ind):
        nonlocal index
        

        mid = len(lst) // 2
        if len(lst) == 1:
            return index#, lst[0]
        else:
            if n >= lst[mid]:
                index += len(lst[:mid])          
                return foo(n, lst[mid:], index)
            else:
                return foo(n, lst[:mid], index)

    index = 0
    print('result:')
    print('    Index =', foo(num, nums, index))#[0])

    
def no_rec1(n):
    d = {}
    for i, v in enumerate(nums):
        d.update([(v, i)])
    print('result:')
    print('    Index =', d[n])
            
        
def no_rec2(n):
    i = 0
    a = nums[:]
    while len(a) != 1:
        mid = len(a) // 2
        if n >=a[mid]:
            i += mid
            a = a[mid:]
        else:
            a = a[:mid]
    print('Result:')
    print('    index =', i)
            

    
nums = sorted([random.randint(1, 1000) for i in range(100)])
version = input('"y" если с рекурсией, "n" если без --> ')
print('List:\n',nums)
num = int(input('Input your number: '))
print('zagadannoe chslo', num)
if num in nums:
    if version == 'y': 
        rec(num)
    else:
        x = int(input('1й или 2й вариант?: '))
        if x == 1:        
            no_rec1(num)
        else:
            no_rec2(num)
else:
    print('Your number not in list')
