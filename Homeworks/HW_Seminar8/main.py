# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def write_file(data_list):
    with open('Phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(data_list + '\n')

def read_file():
    with open('Phonebook.txt', 'r+', encoding='utf-8') as file:
        return file.read()

def enter_user():
        surname = input('Введите фамилию: ') + ' '
        name = input('Введите имя: ') + ' '
        patronymic = input('Введите отчество: ') + ' '
        age = input('Введите возвраст: ') + ' '
        phone_number = input('Введите номер телефона: ') + ' '
        return (surname + name + patronymic + age + phone_number)

def data_search():
    element = input('Введите характеристику для поиска: ')
    for user in read_file().split('\n'):
        for user_element in user.split():
            if user_element.lower() == element.lower():
                print(user)

def add_user():
    write_file(enter_user())

def show_data():
    print(read_file())

def database_operations():
    print('Для добавления данных введите "add": ')
    print('Для поиска данных введите "find": ')
    print('Для вывода всего справочника введите "show": ')

    request = input('Введите: ')

    if request == 'add':
        add_user()
    elif request == 'find':
        data_search()
    elif request == 'show':
        show_data()
    else:
        print("Введите другой запрос!")

database_operations()






