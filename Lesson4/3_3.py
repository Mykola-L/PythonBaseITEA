my_list = [1,2,3,4,5,1,2,2,5,3,3,7,7,8,8,9]


# Цикл while викликає функцію багато разів
i = 0

#my_list.count(i) # повертає кількість елементів із значенням i
my_list2 = []

a = 0
for i in my_list:
    my_list2.append(my_list.count(i))
    i = i + 1
print(my_list2)
#return a