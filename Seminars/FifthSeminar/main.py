# Задача №31.
# # Последовательностью Фибоначчи называется
# # последовательность чисел a0, a1, ..., an, ..., где a0= 0, a1= 1, ak = ak-1 + ak-2 (k > 1).
# # Требуется найти N-е число Фибоначчи
# # Input: 7
# # Output: 21

# m = int(input("Введите необходимое количество чисел Фибоначчи: "))
# n = int(input("Введите число N: "))
# def fib(m):
#     if m in [1, 2]:
#         return 1
#     else:
#         return fib(m - 1) + fib(m - 2)
#
# list1 = []
#
# for i in range(1, m):
#     list1.append(fib(i))
#
#
# print(list1)
# print(list1[n])


# Задача №33.
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
#
# import random
#
# n = int(input("Введите число N: "))
#
#
# some_list = []
# for i in range(n):
#     some_list.append(random.randint(1, 5))
# print(some_list)
#
# def correction_of_grades(m):
#     for i in range(len(some_list)):
#         if some_list[i] > 3:
#             some_list[i] = 1
#     print(some_list)
#
# correction_of_grades(some_list)

# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# n = int(input("Введите число N: "))
#
# def prime_number (number):
#     if n > 1:
#         for i in range(2, int(n/2) + 1):
#             if n % i == 0:
#                 print("no")
#                 break
#         else:
#             print("yes")
#     else:
#         print('no')

# prime_number(n)

# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
import random

# n = int(input('Введите количество элементов последовательности: '))
#
# def rev(n):
#     if n == 0:
#         return ''
#     num = int(input("Введите число: "))
#     return rev(n-1) + f'{num}'
#
#
# print(rev(n))



