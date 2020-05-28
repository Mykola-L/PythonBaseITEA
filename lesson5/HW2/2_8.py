import datetime

a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# '2019-12-30_15-36-11'
print(a3)

# Удалит существующую информацию в some.txt и запишет "Hello".
#my_file = open("a3.txt", 'a')
#my_file = open("a3.txt", 'w')
my_file = open("a3.txt", 'w')
my_file.write("Hello")
my_file.close()


i=1
while i > 0:
    a1 = input('Введіть, будь-ласка, будь-які, дані з клавіатури ')
    # Оставит существующую информацию в some.txt и добавит "Hello".
    my_file = open("a3.txt", 'a')
    my_file.write("Hello2")
    my_file.close()
    i += 1 # i = i + 1