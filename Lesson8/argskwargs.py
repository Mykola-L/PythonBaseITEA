# def tes_smth(arg1, arg2, arg3=5):
#     return (arg1, arg2, arg3)
#
# r = tes_smth(5, arg3=1, arg2=10) # передаємо аргументи як позиційні
#
# print(r)

def my_sum(arg1, *args, default_1=None, **kwargs):
    s = 0 # визначаємо суму всіх елементів функції my_sum
    print(kwargs)
    print(default_1)
    for number in args:
        s += number
    return s

list_of_numbers = [6, 100, 22, 4, 2, 2, 3, 4, 5, 12]
dict_of_data = {'four': 4, 'six': 6, 'eight': 8}
# r = my_sum(*list_of_numbers, four=4, six=6, eight=8) # розпаковую всі елементи списку, перетворюю кожен в окремий елемент
# вверху те що внизу, але словник розпакований
r = my_sum(*list_of_numbers, default_1=4, **dict_of_data)

print(r)

# розпаковка
#*[1, 3, 4, 5, 6] => 1, 3, 4, 5, 6 # потрібно перетворити список в 5 окремих елементів
# операція зняття дужок називається розпаковкою
