'''На прошлой неделе мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую
тексту, сжатому с помощью кодирования повторов, и производит обратную
операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это
задание.

В исходном тексте не встречаются цифры, так что код однозначно
интерпретируем.


'''


import re


s = ''
with open('dataset_3363_2(4).txt', 'r') as file:
    s = file.read().strip()
    
nums = []
syms = []
nums.extend(re.findall(r'\d+', s))
syms.extend(re.findall(r'\D', s))
dif = []

for i, el in enumerate(syms):
    x = el + nums[i]
    dif.append(x)

res = ['' for m in dif]
for i, el in enumerate(dif):
    res[i] = el[0] * int(el[1:])


print(res)
with open('outputfile.txt', 'w') as out:
    out.write(''.join(res))
