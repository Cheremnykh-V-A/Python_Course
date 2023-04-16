# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

N = int(input("Введите число N: "))
x = int(input("Введите число Х: "))
next_x = 0

some_list = []
for i in range(N):
    some_list.append(random.randint(1, 10))

some_set = set(some_list)
some_list_new = list(some_set)
some_list_new.sort()

for i in range(len(some_list_new)):
    if x > max(some_list_new):
        next_x = max(some_list_new)
    elif some_list_new[i] > x:
        next_x = some_list_new[i]
        break
    elif max(some_list_new) < N:
        next_x = max(some_list_new)

print(some_list)
print(some_list_new)
# print(some_list_new)
print(next_x)

