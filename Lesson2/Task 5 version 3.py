my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_items_list = len(my_list)
#print(number_items_list)

arraySum = 0
i = 0
while i < number_items_list:
    arraySum = arraySum + my_list[i]
    i+=1

print(arraySum)
