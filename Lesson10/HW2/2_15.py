# bind
from tkinter import Tk, Toplevel, Button, Label, Entry, END, Listbox, SINGLE
import random
import time
import datetime
import json
# import pprint
from pprint import pprint #подключили Pprint для красоты выдачи текста
import keyboard

# визначає час
a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(a3)

root = Tk() # головне вікно

def game_launch(): # кнопка запуск гри
    time1 = time.time() # час початку введення фрази користувачем
    print(f'time1 {time1}')
    # обираю випадкову фразу з файлу
    file = open('list_random_phrases.txt', 'r')
    r = file.readlines()
    print(f'r{r}')
    r2 = [line.rstrip() for line in r] # забираємо \n
    print(f'r2{r2}')
    random_phrase = random.choice(r2) # random_phrase - випадкова фраза
    print(f'random_phrase game_launch: {random_phrase}')
    file.close()

    entry = Entry(width=256) # користувач вводить текст

    label1 = Label(text='Введіть текст випадкової фрази:', font='Arial 20') # віджет призначений для відображення напису
    label2 = Label(text=f'{random_phrase}', font='Arial 20') # віджет призначений для відображення напису
    label1.pack()  # упаковуємо кнопку label
    label2.pack()  # упаковуємо кнопку label
    entry.pack()  # упаковуємо кнопку entry

    #return time1, random_phrase, entry

    def random_phrase_entered():  # кнопка випадкову фразу введено
        path = entry.get()  # користувач вводить текст
        print(f'path entry random_phrase_entered 1: {path}')
        if str(random_phrase) == str(path):  # якщо випадкова фраза = введеній фразі
            print(f'random_phrase random_phrase_entered: {random_phrase}')
            print(f'path entry random_phrase_entered 2: {path}')
            time2 = time.time()  # час завершення введення фрази користувачем
            print(f'time2: {time2}')
            time3 = time2 - time1 # швидкість набору тексту користувачем
            print(f'time3: {time3}') # швидкість набору тексту користувачем
            print(f'Швидкість набору тексту користувачем: {time3} с.')


            # метод bind - зв'язувати
            # аргументи: self, sequence, func, add
            # sequence - послідовність, add - додати
            # функція яка рахує скільки разів користувач натиснув клавішу backspace
            # pressed the key - натиснув клавішу

            # def pressed_the_key_backspace():
                # for i in entry:

            while True:  # making a loop - виготовлення петлі циклу
                try:  # used try so that if user pressed other than the given key error will not be shown
# Використовуйте try спробуйте, щоб у випадку, якщо користувач натиснув інакше, ніж вказана помилка клавіші, не відображатиметься
                    count = 0
                    if entry.keyboard.is_pressed('backspace'):  # if key 'a' is pressed
                        count = count + 1
                        print('You Pressed backspace Key!')
                        break  # finishing the loop
                    else:
                        pass # пропуск
                except:
                    break  # if user pressed other than the given key the loop will break

            a4 = entry.bind('backspace')
            print(f'bind: {a4}')


            tl1 = Toplevel(root)  # друге вікно
            tl1.title('Ви ввели фразу вірно')
            tl1.label3 = Label(tl1, text='Ви ввели фразу вірно')
            tl1.label4 = Label(tl1, text=f'Швидкість набору тексту: {time3} с.')
            tl1.label3.pack()  # упаковуємо кнопку label
            tl1.label4.pack()  # упаковуємо кнопку label

            # записує в файл json
            JSON_FILE_NAME = 'result_games.json' # файл результат гри The result of the game

            my_obj = {'Date and time of the game': a3, # Дата і час початку гри
                      'Typing speed seconds': time3, # Швидкість набору тексту
                      # 'Number of errors': b2, # Кількість помилок
                      # 'Number of fixes': b3 # Кількість виправлень
                      }  # створюю об'єкт

            file_json = open(JSON_FILE_NAME, 'a')
            # json.dump(my_obj, file_json)  # метод json.dump серіалізує об'єкт в файл, записує дані не у змінну а у файл.
            json.dump(my_obj, file_json, indent="")  # метод json.dump серіалізує об'єкт в файл, записує дані не у змінну а у файл.
            file_json.close()

        else:
            # виводить на екран кількість різних елементів
            list_1 = list(random_phrase)
            list_2 = list(path)
            sum(a != b for a, b in zip(list_1, list_2))
            abs(len(list_1) - len(list_2))

            difference = sum(a != b for a, b in zip(list_1, list_2))
            difference += abs(len(list_1) - len(list_2))
            print(difference)

            tl3 = Toplevel(root)  # друге вікно
            tl3.title('Ви ввели невірну випадкову фразу.')
            tl3.label5 = Label(tl3, text='Ви ввели невірну випадкову фразу.')
            tl3.label6 = Label(tl3, text=f'Кількість помилок: {difference}')
            tl3.label5.pack()  # упаковуємо кнопку label
            tl3.label6.pack()  # упаковуємо кнопку label

            print(f'Ви ввели невірну випадкову фразу. Кількість помилок: {difference}')




    button3 = Button(root,  # кнопка
                     text='Випадкову фразу введено',
                     fg='black',
                     bg='yellow',
                     font='Arial 20',  # розмір шрифта напису на кнопці
                     width=200,
                     height=5,
                     command=random_phrase_entered
                     )

    button3.pack()

def result_games():
    tl2 = Toplevel(root) # друге вікно
    tl2.title('Результат ігор')

# переводимо json у словник формат Python
    file_json = open('result_games.json', 'r')  # 'r' файл відкритий на читання
    res = json.load(file_json)  # метод json.load десеріалізує об'єкт з файлу, бере дані з файлу і записує в словник
    # my_list
    file_json.close()
    pprint(res)
    print(f'Виводить результат ігор з файлу json {res}')
    print(f'Тип змінної, писку {type(res)}') # виводить тип змінної, списку

# переводимо словник формат Python у кортеж
    values_list = [] # словник res пертворюємо в котеж values_list
    for i in res.items():
        values_list.append(i)
        print(f'словник повертається як кортеж {i}')
    print(f'словник перетворюємо в кортеж {values_list}')

# кортеж переводимо у список і через Listbox відправляємо на друге вікно
    listbox = Listbox(tl2, height=50, width=150, selectmode=SINGLE)
    list_of_files = list(values_list) # кортеж values_list переводимо у список list
    for i  in list_of_files:
        listbox.insert(END, i)
    listbox.pack()

button1 = Button(root, # кнопка
                text='Запуск гри',
                fg='black',
                bg='green',
                font='Arial 20', # розмір шрифта напису на кнопці
                width=200,
                height=5,
                command=game_launch
                )

button2 = Button(root, # кнопка
                text='Перегляд історії ігор',
                fg='black',
                bg='orange',
                # fg='white',
                # bg='purple',
                font='Arial 20', # розмір шрифта напису на кнопці
                width=200,
                height=5,
                command=result_games
                )

root.title('Game') # написали заголовок у вікні
root.geometry('1200x800') # розміри вікна: ширина 600, висота 400



button1.pack() # упаковуємо кнопку
button2.pack()


root.mainloop() # mainloop() це метод який запустить нашу програму в безкінечному циклі.