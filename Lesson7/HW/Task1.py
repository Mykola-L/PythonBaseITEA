# 1) Создать приложение записной книги с помощью модуля Tkinter.
# Пользователь вводит следующую информацию о контакте:
# Имя, Фамилия, Номер телефона, Адрес.
# По нажатию на кнопку сохранить,новый контакт должен записываться в файл,
# так же должно сохраниться время создания контакта.
# При нажатии на кнопку «Мои контакты» выводить все доступные контакты (из
# файла) в новом окне. В новом окне создать кнопку («Очистить список»), при
# нажатии на которую файл с контактами будет очищаться и окно с контактами
# будет закрыто.

from tkinter import Tk, Toplevel, Button, Label, Entry, Text, END, Listbox, SINGLE
import datetime

a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(a3)

root = Tk()

entry1 = Entry(width=256, font='Arial 20')
entry2 = Entry(width=256, font='Arial 20')
entry3 = Entry(width=256, font='Arial 20')
entry4 = Entry(width=256, font='Arial 20')

def save1():
    my_file = open("my_contacts.txt", 'a')
    my_file.write(
        f" Contact creation time: {a3} \n Name: {entry1.get()} \n Surname: {entry2.get()} \n Phone number: {entry3.get()} \n Address: {entry4.get()} \n \n")
    my_file.close()


def window2():
    tl = Toplevel(root)
    tl.title('Нове вікно. Мої контакти')
    print('A')

    with open('my_contacts.txt', 'r') as f:
        nums = f.readlines()
    print(nums)
    f.close()
    print('B')

    listbox = Listbox(tl, height=50, width=150, selectmode=SINGLE)
    list_of_files = nums
    for i in list_of_files:
        listbox.insert(END, i)
    listbox.pack()

    def clear_list():
        open('my_contacts.txt', 'w').close()
        tl.withdraw()

    button3 = Button(tl,
                     text='Очистити список',
                     fg='white',
                     bg='purple',
                     width=125,
                     height=10,
                     command=clear_list
                     )
    button3.pack()


label1 = Label(text="Введіть інформацію про контакт: ім'я", font='Arial 10')
label2 = Label(text="Введіть інформацію про контакт: прізвище", font='Arial 10')
label3 = Label(text="Введіть інформацію про контакт: номер телефону", font='Arial 10')
label4 = Label(text="Введіть інформацію про контакт: адресу", font='Arial 10')

button = Button(root,
                text='Мої контакти',
                fg='red',
                bg='green',
                width=600,
                height=10,
                command=window2
                )

button2 = Button(root,
                 text='Зберегти',
                 fg='red',
                 bg='orange',
                 width=600,
                 height=10,
                 command=save1
                 )

root.title('Записна книга')
root.geometry('600x600')

button.pack()
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label4.pack()
entry4.pack()
button2.pack()

root.mainloop()
