import datetime

a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#print(a3)




i=1
while i > 0:
    a1 = input('Введіть, будь-ласка, будь-які, дані з клавіатури ')

    my_file = open("Task2_1.txt", 'a')
    my_file.write(f'{a3}: {a1} \n' )

    # my_file.write(a3)
    # my_file.write(': ')
    # my_file.write(a1)
    # my_file.write('\n')
    my_file.close()

    i += 1 # i = i + 1