import random
import datetime


a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(a3)
# функція декоратор (ім’я довільне)
def decorator(func): # функція декоратор приймає на вхід функцію яку потрібно змінити
# ім'я функції може бути будь-яке
# func об’єкт цільової функції

# (ім’я довільне, але прийнято використовувати wrapper)
    def wrapper():  # декоратор всередині містить іншу функцію wrapper, тут зберігається та поведінка яку ми будемо додавати до вихідної функції.
# wrapper те як ми будемо функцію змінювати, змінена цільова функція.
# wrapper може приймати деякі аргументи
# wrapper має приймати ту ж кількість цільових аргументів, які приймає цільова функція.
        my_file = open("Logs.txt", 'a')
        my_file.write(f'{a3}: {b} \n')

        my_file.close()
    func()


    return wrapper # функція повертає об'єкт wrapper
# функція декоратор має повертати об'єкт wrapper (обгортка)

# функція цільова
@decorator # відмічаємо функцію декоратор, назва функції
def password_generator(a):
    length = a
    passwd = list('1234567890abcdABCD!@#$%^&*()-=_?qwertySDFGH')
    random.shuffle(passwd)
    passwd = ''.join([random.choice(passwd) for x in range(length)])
    print(passwd)  # шкиd69#&



    #i += 1  # i = i + 1

    return passwd




password_generator(8)

b = password_generator