# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого списка: "))

some_list1 = []

for i in range(0, n):
    elements1 = int(input(f"Введите {i} элемент списка: "))
    some_list1.append(elements1)
print(some_list1)
print()

m = int(input("Введите количество элементов второго списка: "))

some_list2 = []

for j in range(m):
     elements2 = int(input(f"Введите {j} элемент второго списка: "))
     some_list2.append(elements2)
print(some_list2)
print()

some_set1 = set(some_list1)
some_set2 = set(some_list2)

some_set3 = some_set1.union(some_set2)
some_list3 = list(some_set3)
some_list3.sort()

print(f"Объединенный список без повторений {some_list3}")
