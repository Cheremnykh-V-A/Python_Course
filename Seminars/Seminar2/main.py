# Вводятся числа, пока не введут 0. Найти сумму четных чисел
import random

# a = [1, 2, 3, 4, -5]
# ind = 0
# while ind < len(a):
#     if a[ind] < 0:
#         print('YES')
#         break
#     ind += 1
# else:
#     print('No')

# Значение переменной-итератера используется
# for i in range(1, 11):
#     print(i ** 2)


# Значение переменной-итератера не используется
# for _ in range(100, 110, 2):  # 0, 1, 2, 3, 4
#     print('HELLO')

# some_list = [-3, 4, 5, 0, 1]
# for a in some_list:
#     print(a)
#
# for ind in range(0, len(some_list)):  # 0, 1, 2, 3, 4
#     print(some_list[ind])


# a = []
# a.append(10)
# print(a)
#
#
# a = []
# print(a)
# a[1] = 200
# a[2] = 300
# print(a)

# 9. По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# n = int(input("Введите число N: "))
# count = 1
# fact = 1
# while count <= n:
#     fact = fact * count
#     count += 1
# print(fact)

# 11.Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n) = A.Если А не является числом Фибоначчи, выведите число - 1.

# n = int(input("Введите число: "))
#
# a = 0
# b = 1
# c = 1
# i = 2
#
# while c < n:
#     c = a + b
#     a = b
#     b = c
#     i += 1
#
#
# if n == c:
#     print(f"Позиция числа: {i}")
# elif n == 0:
#     print("Позиция числа: 0")
# elif n == 1:
#     print("Позиция числа: 1 либо 2")
# else:
#     print("Такого значения нет!")

# Решение методом рекурсии
# def fibo(n):
#     if n <=0:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# print(fibo(5))

#
# 13. 1. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# n = int(input("Введите количество рассматриваемых дней: "))
# temp = []
# positiv_temp = 0
# negativ_temp = 0
# count = 0
# max_positiv_days = 0
# for i in range(n):
#     temp.append((random.randint(-50, 50)))
#     if temp[i] > 0:
#         positiv_temp += 1
#         count = positiv_temp
#         if max_positiv_days < count:
#             max_positiv_days = count
#
#     else:
#         positiv_temp = negativ_temp
#
# print(temp)
# print(max_positiv_days)

# 15. Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий
# и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# n = int(input("Введите количество арбузов: "))
# max = 0
# min = 30000
# weight = []
#
# for i in range(n):
#     weight.append(random.randint(1, 30000))
#     print(f"Масса 1 арбуза равна {weight[i]} ")
#     if weight[i] > max:
#         max = weight[i]
#     elif weight[i] < min:
#         min = weight[i]
# print()
# print(f"Масса самого лёгкого арбуза = {min}")
# print(f"Масса самого тяжёлого арбуза = {max}")