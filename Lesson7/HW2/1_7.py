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
# from tkinter import Tk, Listbox, SINGLE, END
# з модуля tkinter import Tk
# Tk це клас на основі якого ми будемо створювати наш додаток.
import datetime

# визначає час
a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(a3)

# ми створюємо змінну об'єкт Root, кореневе вікно, найголовніше в програмі, через яке пройдуть всі маніпуляції з іншими вікнами віджетами.
# наша програма буде виконуватися в одному великому безкінечному нескінченому циклі.

root = Tk()  # 1. викликаю Tk() як функцію, і передаємо її результат в змінну root

# tl = Toplevel(root) #2. root віджет до якого прив'язане другорядне вікно
# tl.title('Нове вікно. Мої контакти')
# text1.get('1.0', tl.END)
# tl.text = my_file

# txt = Text(height=10, width=256)
# аргумент height= висота, кількість рядків,
# аргумент width= 256 символів ми можемо ввести

# # беремо текст який ввів користувач в entry і записуємо його в label
# def get_name(): # створюємо функцію, аргументи вона приймати не буде, вона буде працювати з глобальними змінними entry і label
#     label.configure(text='Ім"я') # все що ввів користувач в entry, записую в label
#     entry.delete(0, END) # очищаємо entry з нульового по останній елемент, метод delete - очищає, import END
# #entry.delete(2, 4)  # можна видалити 2 і 4 символ


# Метод configure потрібен для того, щоб змінювати наш об’єкт в процесі виконання.

# створимо якусь функцію і протестуємо її
# функції для активації віджетів, передаються в конструктор цих віджетів в якості аргумента command,
# відповідно замість виклику функції передаємо саме об'єкт функції без (). Функція це об'єкт.

entry1 = Entry(width=256, font='Arial 20')
entry2 = Entry(width=256, font='Arial 20')
entry3 = Entry(width=256, font='Arial 20')
entry4 = Entry(width=256, font='Arial 20')


# зберігаємо в файл введену користувачем інформацію
def save1():
    my_file = open("my_contacts.txt", 'a')
    my_file.write(
        f" Contact creation time: {a3} \n Name: {entry1.get()} \n Surname: {entry2.get()} \n Phone number: {entry3.get()} \n Address: {entry4.get()} \n \n")

    my_file.close()


# tl.text = save1()

def window2():  # функція для вікна 2
    tl = Toplevel(root)  # 2. root віджет до якого прив'язане другорядне вікно
    # виводить на екран вікно 2
    tl.title('Нове вікно. Мої контакти')
    print('A')


    with open('my_contacts.txt', 'r') as f:  # зчитуємо файл
        nums = f.readlines()
    print(nums)
    # tl.label(nums)
    f.close()
    print('B')

# виводимо контакти в новому вікні
    # root = Tk()
    listbox = Listbox(tl, height=50, width=150, selectmode=SINGLE)
    # entry це те що можна вводити, listbox це те, що можна дивитися, воно буде списком
    # розмір Listbox можна зміювати як нам зручно
    # list_of_countries = ["Ukraine", "Moldova", "Poland"]
    list_of_files = nums
    for i in list_of_files:
        listbox.insert(END, i)
    listbox.pack()
    # root.mainloop()

# очищуємо список, закриваємо вікно
    def clear_list():
        open('my_contacts.txt', 'w').close() # очищуємо файл
        

    button3 = Button(tl,
                     text='Очистити список',
                     fg='white',
                     bg='purple',
                     width=125,
                     height=10,
                     command=clear_list
                     )
    button3.pack()

# font='Arial 20' змінюємо шрифт
# аргумент width= 256 символів ми можемо ввести
# аргумент show= актуальний коли хочете зробити поле для введення паролю, наприклад.
# якщо введу *, то кожен символ в цьому рядку буде відображатися як *
# label = Label(text="Введіть інформацію про контакт: ім'я, прізвище, номер телефону, адресу", font='Arial 10')
label1 = Label(text="Введіть інформацію про контакт: ім'я", font='Arial 10')
label2 = Label(text="Введіть інформацію про контакт: прізвище", font='Arial 10')
label3 = Label(text="Введіть інформацію про контакт: номер телефону", font='Arial 10')
label4 = Label(text="Введіть інформацію про контакт: адресу", font='Arial 10')

# font='Arial 20' змінюємо шрифт
# віджет призначений для відображення напису
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

# перший аргумент - віджет до якого прив'язана кнопка.
# 2 аргумент текст, текст який буде написаний на кнопці,
# 4 аргумент bg - колір кнопки, 16-річна система
# 3 аргумент fg - колір тексту на кнопці
# 5 аргумент font - шрифт і його розмір
# 6 аргумент width, height - ширина і довжина кнопки


root.title('Записна книга')  # написали заголовок у вікні
root.geometry('600x600')  # розміри вікна: ширина 600, висота 400

button.pack()  # упаковуємо кнопку
label1.pack()  # упаковуємо label
entry1.pack()  # упаковуємо entry
label2.pack()  # упаковуємо label
entry2.pack()  # упаковуємо entry
label3.pack()  # упаковуємо label
entry3.pack()  # упаковуємо entry
label4.pack()  # упаковуємо label
entry4.pack()  # упаковуємо entry
button2.pack()  # упаковуємо кнопку

# txt.pack() # упаковуємо text
root.mainloop()  # mainloop() це метод який запустить нашу програму в безкінечному циклі.
# порядок упаковки, що за чим буде у вікні, в якому порядку ви їх упакуєте, в такому порядку вони будуть відображені.

# з'явилося два вікна
# вводжу текст в вікні, тисну на кнопку, повністю введений рядок очищається