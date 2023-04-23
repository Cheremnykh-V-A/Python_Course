# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.


def rle_function(string):
    enconding = ''
    count = 1
    prev_char = ''

    if not string:
        return ''
    for char in string:
        if char != prev_char:
            if prev_char:
                enconding += prev_char + str(count)
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += prev_char + str(count)
        return enconding

result = rle_function('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
print(result)