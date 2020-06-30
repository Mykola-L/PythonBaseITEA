from tkinter import Tk, Toplevel, Button, Label, Entry
import random
import time

root = Tk() # головне вікно

tl = Toplevel(root) # друге вікно
tl.title('One more window')

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
        else:
            print('Ви ввели невірну випадкову фразу')

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



root.title('Itea-Lesson-7') # написали заголовок у вікні
root.geometry('1200x800') # розміри вікна: ширина 600, висота 400



button1.pack() # упаковуємо кнопку
button2.pack()


root.mainloop() # mainloop() це метод який запустить нашу програму в безкінечному циклі.