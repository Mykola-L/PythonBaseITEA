# функція декоратор (ім’я довільне)
def decorator(func): # функція декоратор приймає на вхід функцію яку потрібно змінити
# ім'я функції може бути будь-яке
# func об’єкт цільової функції

# (ім’я довільне, але прийнято використовувати wrapper)
    def wrapper():  # декоратор всередині містить іншу функцію wrapper, тут зберігається та поведінка яку ми будемо додавати до вихідної функції.
# wrapper те як ми будемо функцію змінювати, змінена цільова функція.
# wrapper може приймати деякі аргументи
# wrapper має приймати ту ж кількість цільових аргументів, які приймає цільова функція.
        print('decorating function')
        func()
        print('Decoration ended')

    return wrapper # функція повертає об'єкт wrapper
# функція декоратор має повертати об'єкт wrapper (обгортка)

# функція цільова
@decorator # відмічаємо функцію декоратор, назва функції
def start():
    print('Function has been started')

start()
