list_1 = ['a', 'a', 'a', 'b']
list_2 = ['a', 'b', 'b', 'b', 'c']

# виводить на екран кількість різних елементів
sum(a != b for a, b in zip(list_1, list_2))
abs(len(list_1) - len(list_2))

difference = sum(a != b for a, b in zip(list_1, list_2))
difference += abs(len(list_1) - len(list_2))
print(difference)