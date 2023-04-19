# Выведите числа Фибоначчи с номерами от n1 до n2

count = int(input("Введите необходимое количество чисел Фибоначчи: "))
n1 = int(input("Введите число 1: "))
n2 = int(input("Введите число 2: "))

fib1 = 0
fib2 = 1
fib_sum = 0
fib_list = []

for i in range(count):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    fib_list.append(fib_sum)
fib_list.append(0)
fib_list.append(1)
fib_list.sort()
print(fib_list)

print(fib_list[fib_list.index(n1):fib_list.index(n2)+1])





