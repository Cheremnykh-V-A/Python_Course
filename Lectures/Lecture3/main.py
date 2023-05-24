# Функции:
# 1. Необходимо создать функцию sumNumbers(n), которая будет считать сумму всех элементов от 1 до n.
#
# Решение:
# Необходимо создать функцию:

#def sumNumbers(n): # Сколько аргументов передаем, столько и принимаем. В нашем случае функция sumNumbers принимает 1 аргумент n

# def sumNumbers(n):
#     summa = 0
#
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)
#
# sumNumbers(5)

# def sumNumbers(n):
#     summa = 0
#
#     for i in range(1, n + 1):
#         summa += i
#     return summa # для того, чтобы функция возвращала summa
#
# a = sumNumbers(5)
# print(a)

# def sumNumbers(n, y = 'Hello'): # Передаем и принимаем 2 аргумента
#     summa = 0
#     print(y)
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)
#
# sumNumbers(5)

# 2. Передача неограниченного количества аргументов:

# def sum_str(*args): # * означает передачу неограниченного количества аргументов
#     res = ''
#     for i in args:
#         res += i
#     return res
#
# print(sum_str('q', 'e', 'l'))
#-----------------------------------------------------------------------------------------------------------------------
# Вызов функции из другого файла(модуля):
# Сначала обращаемся к модулю, затем пишем название функции.
#
# 1.
# import modul1
#
# print(modul1.max1(5, 9))

# 2.
# from modul1 import max1 # Напрямую импортировать функции
#
# print(max1(5, 10)) # В этом случае название модуля в print писать не нужно

# 3.
# from modul1 import * # * означает то, что мы хотим импортировать сразу все функции из модуля

# 4.
# import modul1 as m1 # Так сокращается название файла из которого импортируем модуль
#
# print(m1.max1(10,8))
#-----------------------------------------------------------------------------------------------------------------------

# Рекурсия:
# При описании рекурсии важно указать, когда функции надо остановиться и перестать вызывать саму себя.

# 1. Пользователь вводит число n. Необходимо вывести n - первых членов последовательности Фибоначчи.

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n - 2)
#
# list_1 = []
#
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)
#-----------------------------------------------------------------------------------------------------------------------

# Алгоритмы:
# Алгоритмом называется набор инструкция для выполнения некоторой.
# Впринципе, любой фрагмент програмного кода можно назвать алгоритмом,
# но мы рассмотрим 2 самых известных алгоритма сортировок:
# 1) Быстрая сортировка
# 2) Сортировка слиянием

# 1. Быстрая сортировка:
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
# print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))

# 2. Сортировка слиянием:
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
#
# list_1 = [1, 5, 9, 6, 8, 7, 2, 1, 55, 2, 4]
#
# merge_sort(list_1)
# print(list_1)





