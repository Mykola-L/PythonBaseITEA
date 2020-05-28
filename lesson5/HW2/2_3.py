import time

i=1
while i > 0:
    a1 = input('Введіть, будь-ласка, будь-які, дані з клавіатури ')

    #b = datetime.strptime(a1, )  # преобразует строку в datetime
    b = time.strptime(a1)
    print(b)
    i += 1 # i = i + 1



# time.time() = a
# f = open((time.time()), "a")
# f.write("Test string")
# 11
# f.close()

# Удалит существующую информацию в some.txt и запишет "Hello".
my_file = open("some.txt", 'w')
my_file.write("Hello")
my_file.close()
# Оставит существующую информацию в some.txt и добавит "Hello".
my_file = open("some.txt", 'a')
my_file.write("Hello")
my_file.close()