from tkinter import Tk, Toplevel, Button, Label, Entry
import random
import time
import config

root = Tk() # головне вікно

tl = Toplevel(root) # друге вікно
tl.title('One more window')

def game_launch(): # кнопка запуск гри
    time1 = time.time() # час початку введення фрази користувачем
    print(time1)
    # обираю випадкову фразу з файлу
    file = open('list_random_phrases.txt', 'r')
    r = file.readlines()
    print(r)
    random_phrase = random.choice(r) # random_phrase - випадкова фраза
    print(random_phrase)
    file.close()

    entry = Entry(width=256) # користувач вводить текст

    label1 = Label(text='Введіть текст випадкової фрази:', font='Arial 20') # віджет призначений для відображення напису
    label2 = Label(text=f'{random_phrase}', font='Arial 20') # віджет призначений для відображення напису
    label1.pack()  # упаковуємо кнопку label
    label2.pack()  # упаковуємо кнопку label
    entry.pack()  # упаковуємо кнопку entry

    return time1, random_phrase, entry

def random_phrase_entered(): # кнопка випадкову фразу введено
    if game_launch.random_phrase == game_launch.entry:  # якщо випадкова фраза = введеній фразі
        print(game_launch.random_phrase)
        print(game_launch.entry)
        time2 = time.time()  # час завершення введення фрази користувачем
        print(time2)
        time3 = time2 - game_launch.time1
        print(time3)


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
                font='Arial 20', # розмір шрифта напису на кнопці
                width=200,
                height=5
                )

button3 = Button(root, # кнопка
                text='Випадкову фразу введено',
                fg='black',
                bg='yellow',
                font='Arial 20', # розмір шрифта напису на кнопці
                width=200,
                height=5,
                command=random_phrase_entered
                )

root.title('Itea-Lesson-7') # написали заголовок у вікні
root.geometry('1200x800') # розміри вікна: ширина 600, висота 400



button1.pack() # упаковуємо кнопку
button2.pack()
button3.pack()

root.mainloop() # mainloop() це метод який запустить нашу програму в безкінечному циклі.

