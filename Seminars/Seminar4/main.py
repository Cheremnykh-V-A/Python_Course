# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# str = 'aaabcaadcdd'
# print(str)
#
# count_dict = {}
# for letter in str:
#     if letter not in count_dict:
#         count_dict[letter] = 1
#     else:
#         count_dict[letter] += 1
# print(count_dict)


# Задача №27.
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# some_str = input()
# some_set = set()
# temp_word = ''
# for letter in some_str:
#     if letter != ' ':
#         temp_word += letter
#     else:
#         if temp_word:
#             some_set.add(temp_word)
#         temp_word = ''
# some_set.add(temp_word)
# print(f'Количество уникальных слов = {len(some_set)}')

# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

# some_list = [1, 4, 3, 9, 8, 11, 0, 13]
# some_list.sort()
# print(some_list)
#
# result_list = []
# temp_list = []
#
# for i in range(0, len(some_list) - 1):
#     if some_list[i + 1] - some_list[i] == 1:
#         temp_list.append(some_list[i])
#     else:
#         temp_list.append(some_list[i])
#         result_list.append(temp_list)
#         temp_list = []
# if temp_list:
#     result_list.append((temp_list))
#
# if some_list[-1] - some_list[-2] == 1:
#     result_list[-1].append(some_list[-1])
# else:
#     result_list.append([some_list[-1]])
#
# print_list = []
# for i in result_list:
#     if len(i) > 1:
#         print_list.append(f'{i[0]}-{i[1]}')
#     else:
#         print_list.append(i[0])
# print(print_list, sep=',')




