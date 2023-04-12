# Списки:
# 1. Способы создания списков:
# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
# print(*list_1)

# for i in list_1:
#     print(i)

# print(len(list_1))

# print(list_1[3])
# print(list_1[-2])
#
# 2. Добавление значений в список:
# list_1 = [1, 5]
# print((list_1))
# list_1.append(8)
# print((list_1))
# list_1.append(85)
# print((list_1))

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)
#
# 3. Функции в списках
# Удаление последнего элемента списка:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# Удаление конкретного элемента списка:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]
#
# 4. Срезы в списках
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1) - 1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1) - 2:]) # [9, 10]
# print(list_1[2: 9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6: -18]) # []
# print(list_1[0: len(list_1): 6]) # [1, 7]
# print(list_1[::6]) # [1,7]
# --------------------------------------------------------
# Кортежи - неизменяемые списки:
# t = () # кортеж
# print(type(t))
#
# t = (1)
# print(type(t))
#
# t = (1, 5, 3, ) # создали кортеж (обязательно нужа запятая в конце)
# print(type(t))
#
# v = [1, 8, 9] # список
# print(v)
# print(type(v))
#
# v = tuple(v) # кортеж
# print(v)
# print(type(v))
#
# # a, b = 1, 2 # прсиваивание
# # a = b = 1 # присваивание
#
# a, b, c = v
# print(a, b, c)

# Отличие кортежа от списка:
# t = (1, 2, 3, 5)
# print(t[1])

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# t[0] = 2 # не выводит, т.к. кортеж изменять нельзя
# --------------------------------------------------------
# Словари - неупорядочные коллекции произвольных объектов с доступом к ключу:
# В списках в качестве ключа используется индекс элемента.
# В словаре для определения элемента используется значение ключа (строка, число).

# d = {} # создали пустой словарь
# d = dict() # создали пустой словарь

# d['q'] = 'qwerty' # в словаре есть ключ 'q', при обращении к которому получаем 'qwerty'
# print(d)
#
# d['w'] = 'werty'
# print(d)
# print(d['q']) # выводит только 'q'

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→ '}
# print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left']) # ←
# # Типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # Типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for(k, v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
#     print(item)
# # up: ↑
# # down: ↓
# # right: →
#
# dictionary[895] = 98998
# print(dictionary)
# --------------------------------------------------------
# Множеста:
# Множесва содержат в себе уникальные элементы, не обязательно упорядоченные

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue', 'gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue', 'gray'}
# colors.clear() # { }
# print(colors) # set()

# Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

#Замороженные множества:
# a = {1, 8, 6}
# b = frozenset(a)
# print(b)
# --------------------------------------------------------
# List Comprehension:
# У каждого языка программирования есть свои особенности и приемущества.
# Одна из культовых фишек Python - list comprehension ("генератор списка").
# List Comprehension - это упрощённый подход к созданию списка, который задействует цикл for,
# а также интсрукции if-else для определения того, что окажется в финальном списке.
#
# 1. Простая ситуация - список:
# list_1 = [exp for item in iterable]
# 2. Выборка по заданному словию:
# list_1 = [exp for item in iterable (if conditional)]

# Задача:
# Создать список, состоящий из четных чисел в диапозоне от 1 до 100.
#
# Решение:
# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1)

# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)]
# print(list_1)

# 2. Добавить условие (только четные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
# print(list_1)

# Допустим вы решили создать пары по каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
# print(list_1)

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1)











