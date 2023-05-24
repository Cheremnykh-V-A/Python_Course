# some_str = 'Hello'
# for letter in some_str:
#     print(letter)

# for ind in range(0, len(some_str)):
#     print(some_str[ind])

# print(some_str[::-1]) # перевернуть строку
#-----------------------------------------------------------------------------
# import random
#
# some_list = []
# for _ in range(10):
#     number = random.randint(1, 10) # заполнение рандомными числами
#     some_list.append(number)
# print(some_list)
#
# print(some_list.count(7)) # поиск 7 в списке
#
# print(7 in some_list)
#------------------------------------------------------------------------------
# Сравнение времени работы алгоритма со списком и с множенством
#
# import random
# import time
# some_list = [random.randint(1, 10000) for i in range(10 ** 7)]
# some_set = set(some_list)
# some_list = list(some_set)
#
# start = time.perf_counter()
# print(11000 in some_list)
# end = time.perf_counter()
# duration1 = end - start
#
# start = time.perf_counter()
# print(11000 in some_set)
# end = time.perf_counter()
# duration2 = end - start
#
# print(duration1 / duration2)
#------------------------------------------------------------------------------
# Задачи:
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# import random
#
# some_list = []
# for _ in range(10):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)
#
# q = set(some_list)
# print(len(q))

# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# import random
#
# n = int(input("Введите количество элементов: "))
# some_list = []
# for _ in range(n):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)
#
# k = int(input("Введите количество чисел, которые нужно сдвинуть: "))
#
# print(some_list[-k:] + some_list[:-k])

# Напишите программу для печати всех уникальных значений в словаре.
# Input: {1: 2, 5: 2, 6: 3} -> 2, 3
# Output: some_dict.values()

# some_dict = {1: 2, 5: 2, 6: 3}
# print(set(some_dict.values()))

# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# import random
#
# count = 0
# some_list = []
# for i in range(10):
#     number = random.randint(1, 10)
#     some_list.append(number)
#     if some_list[i-1] < some_list[i]:
#         count += 1
# print(some_list)
# print(count)






