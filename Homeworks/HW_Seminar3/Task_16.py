# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

N = int(input("Введите число N: "))
x = int(input("Введите число, количество записей которого нужно посчитать: "))

# count = 0
some_list = []

for i in range(N):
    some_list.append(random.randint(1, 5))
    # if some_list[i] == x:
    #     count += 1

print(some_list)
# print(count)
print(some_list.count(x))
