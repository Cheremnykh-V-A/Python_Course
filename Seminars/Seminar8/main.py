# Чтение файла:

# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     for letter in text:
#         print(letter)


# with open('example.txt', 'r', encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line[:-1])

# with open('example.txt', 'r', encoding='utf-8') as file:
#     line = file.readline()
#     while line:
#         print(line[:-1])
#         line = file.readline()


# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text.splitlines())

# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.readlines()
#     print(text)

#-----------------------------------------------------------------------------------------------------------------------
# Запись в файле:

# with open('example.txt', 'w', encoding='utf-8') as file:
#     some_list = ['hello', 'world', 'how', 'are', 'you']
#     for el in some_list:
#         file.write(el + '\n')

#-----------------------------------------------------------------------------------------------------------------------

# Задачи:

# 1. Пользователь вводит кол-во строк, затем сами строки. Нужно записать в новый текстовый файл все эти строки
# Далее пользователь вводит символ, нужно найти кол-во этого символа в новом файле.

# with open('test.txt', 'w') as test:
#     n = int(input())
#     for i in range(n):
#         test.write(input() + '\n')
#
# simbol = input()
# with open('test.txt', 'r') as test1:
#     data = test1.readline()
#     sum = 0
#
#     while data:
#         sum += data.count(simbol)
#         data = test1.readline()
#     print(sum)

# 2.  Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8') as file:
#         file_text = file.read().split('\n')
#         for i in range(len(file_text) - lines, len(file_text)):
#             print(file_text[i])
#
# read_last(2, 'article.txt')

# 3. Документ «article.txt» содержит следующий текст:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

# def longest_words(file):
#     with open('article.txt', 'r', encoding='utf-8') as file:
#         file_text = file.read().replace('\n', ' ')
#     list_text = file_text.split()
#     # print(list_text)
#     len_text = list(map(len, list_text))
#     max_words = list(filter(lambda x: len(x) == max(len_text), list_text))
#     print(max_words)
#
# longest_words('article.txt')
