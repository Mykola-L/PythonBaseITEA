from tkinter import Tk, Button, Label, Entry
import requests

# з модуля tkinter import Tk
# Tk це клас на основі якого ми будемо створювати наш додаток.

# ми створюємо змінну об'єкт Root, кореневе вікно, найголовніше в програмі, через яке пройдуть всі маніпуляції з іншими вікнами віджетами.
# наша програма буде виконуватися в одному великому безкінечному нескінченому циклі.

root = Tk() # викликаю Tk() як функцію, і передаємо її результат в змінну root


# txt = Text(height=10, width=256)
# аргумент height= висота, кількість рядків,
# аргумент width= 256 символів ми можемо ввести

# беремо текст який ввів користувач в entry і записуємо його в label

# функції для активації віджетів, передаються в конструктор цих віджетів в якості аргумента command,
# відповідно замість виклику функції передаємо саме об'єкт функції без (). Функція це об'єкт.


label1 = Label(text='Введіть посилання на файл в інтернеті') # віджет призначений для відображення напису
label2 = Label(text='Введіть шлях, за яким файл буде збережений на пристрій') # віджет призначений для відображення напису
label3 = Label(text="Введіть ім'я і формат файлу") # віджет призначений для відображення напису
entry1 = Entry(width=256) # аргумент width= 256 символів ми можемо ввести
entry2 = Entry(width=256) # аргумент width= 256 символів ми можемо ввести
entry3 = Entry(width=256) # аргумент width= 256 символів ми можемо ввести
# print(entry1.get())
# функція зберегти файл
def save_file(): # створюємо функцію, аргументи вона приймати не буде, вона буде працювати з глобальними змінними entry і label
    # print('Hello') # створимо якусь функцію і протестуємо її
    #if entry1.get() != None:

# зберігаємо файл в поточній директорії
    r = requests.get(entry1.get()) # записуємо в файл html сайту який ввів користувач
    # print(r)
    path2 = entry2.get()
    path3 = entry3.get()

    if path2 != '': # якщо користувач ввів директорію, зберігає в директорію
        a = path2 # a = шлях до директорії
    else:
        a = './'

    if path3 != '':  # якщо користувач ввів директорію, зберігає в директорію
        b = path3  # b = назва файлу
    else:
        s = entry1.get()
        b = (s.split("/")[-1])
        # print(b)
        # b = entry1.get.split("/")[-1]
# не вводить ім'я файлу

# конструкція контекстний менеджер
        #with open('../index3.html', 'w', encoding='utf-8') as file:
    with open(f'{a}{b}', 'wb') as file:
        file.write(r.content) # відповідь з браузера, з кодом сайту, запишу в файл index.html
    # якщо користувач ввів директорію, зберігає в директорію
    # else:
    #     with open('index3.html', 'w', encoding='utf-8') as file:
    #         file.write(r.text) # відповідь з браузера, з кодом сайту, запишу в файл index.html






# аргумент show= актуальний коли хочете зробити поле для введення паролю, наприклад.
# якщо введу *, то кожен символ в цьому рядку буде відображатися як *

button = Button(root,
                text='Зберегти введені дані!',
                fg='red',
                bg='green',
                width=600,
                height=10,
                command=save_file
# функції для активації віджетів, передаються в конструктор цих віджетів в якості аргумента command,
# відповідно замість виклику функції передаємо саме об'єкт функції без (). Функція це об'єкт.
                )
# перший аргумент - віджет до якого прив'язана кнопка.
# 2 аргумент текст, текст який буде написаний на кнопці,
# 4 аргумент bg - колір кнопки, 16-річна система
# 3 аргумент fg - колір тексту на кнопці
# 5 аргумент font - шрифт і його розмір
# 6 аргумент width, height - ширина і довжина кнопки



root.geometry('600x400') # розміри вікна: ширина 600, висота 400


label1.pack() # упаковуємо label
entry1.pack() # упаковуємо entry
label2.pack() # упаковуємо label
entry2.pack() # упаковуємо entry
label3.pack() # упаковуємо label
entry3.pack() # упаковуємо entry
button.pack() # упаковуємо кнопку

# txt.pack() # упаковуємо text
root.mainloop() # mainloop() це метод який запустить нашу програму в безкінечному циклі.
# порядок упаковки, що за чим буде у вікні, в якому порядку ви їх упакуєте, в такому порядку вони будуть відображені.

# з'явилося два вікна
# при кожному кліку на кнопку виводиться Hello, моя функція get_name активується.