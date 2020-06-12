# def get_fullname(name, surname): # приймає два аргументи: ім'я, прізвище і повертає нам ці аргументи.
#     return f'{name.capitalize()} {surname.capitalize()}'
# # метод capitalize() робить початок рядка з великої букви
#
# print(get_fullname('mykola', 'lavrushko')) # функція з викликом
# print(get_fullname) # функція без виклику
#
# # new_function = get_fullname # функція без виклику є об'єктом
# # # змінна new_function посилається на функцію get_fullname
# # # об'єкт new_function є перехідником на функцію get_fullname
# # print(new_function('mykola', 'lavrushko')) # можна викликати new_function і передати в неї аргументи




def test_func(func, message): # функція test_func викликає іншу функцію func
    # test_func це функція вищого порядку, вона в якості аргумента чекає об'єкт іншої функції
    # функції в Python є об'єктом як і все інше.
    func()
    print(message)

def hello_world():
    print('Hello World')

test_func(hello_world, 'Hi') # hello_world - обєкт функції, функція без виклику

