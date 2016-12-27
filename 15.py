'''
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на
наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть
больше одной строки) и выводит самое частое слово в этом тексте и через
пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
'''

with open('dataset_3363_3.txt', 'r') as file:
    text = file.read().lower().strip().split()

x = 0
max_count_word = ''
for word in text:
    if text.count(word) > x:
        x = text.count(word)
        max_count_word = word
    elif text.count(word) == x:
        max_count_word = word if word < max_count_word else max_count_word
with open('outputfile.txt', 'w') as f:
    f.write(str(max_count_word) + ' ' + str(x))

#print(max_count_word, x)
