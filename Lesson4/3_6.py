from collections import Counter

#array = ["Bob", "Alex", "Bob", "John"]
array = [1, 9, 1, 2, 2, 3, 2, 2, 4, 4, 4, 6, 5, 4]

c = Counter(array)
print(c)

start_dict = dict(c) # переводимо кортеж в словник
# start_dict = Counter(array)

# c
# Counter({'Bob': 2, 'Alex': 1, 'John': 1})
#
# c['Bob']
# 2
#
# c['Unknown']
# 0

print(start_dict)

#a = max(c)


max_value = max(start_dict.values())
final_dict = {k: v for k, v in start_dict.items() if v == max_value}

print(max_value)
print(final_dict)

#my_dict = {'key': 'value'}
my_dict_length = len(final_dict)
print(final_dict)

if my_dict_length > 1:
    a = max(final_dict.keys())
    print(f'Елемент який повторюється найчастіше {a}')
else:
    print(final_dict)