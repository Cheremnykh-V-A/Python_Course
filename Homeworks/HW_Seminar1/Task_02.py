# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трёхзначное число: "))

if (number > 99 and number < 1000):
    a = int(number / 100)
    b = int((number / 10) % 10)
    c = int(number % 10)

    sum = a + b + c

    print(sum)

else:
    print("Введите трёхзначное число!")
