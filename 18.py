'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит
имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл
из этого набора. 

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''
from requests import *


with open('dataset_3378_3.txt', 'r') as file:
    u = file.read().strip()
print('u =', u, end='\n\n')
content = get(u).text
x = 0
print('content =', content, end='\n\n')
while True:
    if content.split()[0] != 'We':
        content = get(
            'https://stepic.org/media/attachments/course67/3.6.3/' + content
            ).text
        x += 1
        print(x, content)
        
    else:
        with open('outputfile.txt', 'w') as f:
            f.write(content)
        break
