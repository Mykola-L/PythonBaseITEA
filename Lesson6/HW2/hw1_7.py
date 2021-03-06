import random
import datetime

a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(a3)


# функція декоратор (ім’я довільне)
def decorator(func):  # функція декоратор приймає на вхід функцію яку потрібно змінити
    # ім'я функції може бути будь-яке
    # func об’єкт цільової функції

    # (ім’я довільне, але прийнято використовувати wrapper)
    def wrapper(arg1):  # декоратор всередині містить іншу функцію wrapper, тут зберігається та поведінка яку ми будемо додавати до вихідної функції.
        # wrapper те як ми будемо функцію змінювати, змінена цільова функція.
        # wrapper може приймати деякі аргументи
        # wrapper має приймати ту ж кількість цільових аргументів, які приймає цільова функція.
        my_file = open("logs.txt", 'a')
        my_file.write(f'{a3}: {arg1} \n')

        my_file.close()

        result = func(arg1)
        print(arg1)
        return result

    return wrapper  # функція повертає об'єкт wrapper


# функція декоратор має повертати об'єкт wrapper (обгортка)

# функція цільова
@decorator  # відмічаємо функцію декоратор, назва функції
def start(arg1):
    print(arg1)  # Функція була запущена
    return 99


start(9)