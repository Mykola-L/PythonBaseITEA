import datetime

a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') # визначаємо поточні час і дату
# '2019-12-30_15-36-11'
print(a3)




i=1
while i > 0:
    a1 = input('Введіть, будь-ласка, будь-які, дані з клавіатури ')

    # Удалит существующую информацию в some.txt и запишет "Hello".
    # my_file = open("a3.txt", 'a')
    # my_file = open("a3.txt", 'w')
    # my_file = open("some4.txt", 'w')
    # my_file.write(a1)
    # my_file.close()

    # Оставит существующую информацию в some.txt и добавит "Hello".
    my_file = open("some13.txt", 'a')
    my_file.write(a3)
    my_file.write(': ')
    my_file.write(a1)
    my_file.write('\n')
    my_file.close()

    i += 1 # i = i + 1