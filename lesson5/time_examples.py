import time

# t = time.time()
#
# print(time.ctime(t))
#
# date_struct = time.localtime() # повернеться кортеж
#
# formated = time.strftime('Number %d Month number %m year %y', date_struct) # другий аргумент приймає змінну, перший аргумент приймає формат. Крапка біля формату, значення я хочу бачити через крапку
# print(formated)

# print('Hello')
# time.sleep(5) # програма зупиняється на 5 секунд.
# print('World')

a = 5
b = 10

def number_func(a, b):
    # if a == b or abs(a-b) == 5 or a + b == 5: # Варіант 1
    return any([a == b, abs(a-b) == 5, a + b == 5]) # ми позбулися or

