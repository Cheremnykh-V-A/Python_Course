# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

number = int(input("Введите число: "))

const = 6 #соотношение 1:4:1

if number % 2 == 0:
    p = int(number / const) #количество журавликов Пети
    s = p #уоличество журавликов Сережи
    k = int(p * 4) #((p + s) * 2) количество журавликов Кати

    print(p, k, s)

else:
    print("Журавликов должно быть чётное количество)")