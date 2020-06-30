from tkinter import Tk, Toplevel, Button, Label, Entry
import random
import time
import config

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
    random_phrase = random.choice(r) # random_phrase - випадкова фраза
    print(f'random_phrase game_launch: {random_phrase}')
    file.close()

    entry = Entry(width=256) # користувач вводить текст
    #path = entry.get() # користувач вводить текст
    print(f'entry game_launch: {entry}')



    label1 = Label(text='Введіть текст випадкової фрази:', font='Arial 20') # віджет призначений для відображення напису
    label2 = Label(text=f'{random_phrase}', font='Arial 20') # віджет призначений для відображення напису
    label1.pack()  # упаковуємо кнопку label
    label2.pack()  # упаковуємо кнопку label
    entry.pack()  # упаковуємо кнопку entry







    def random_phrase_entered(): # кнопка випадкову фразу введено
        # if str(random_phrase) == str(entry):  # якщо випадкова фраза = введеній фразі
        #     print('Ви ввели не вірну випадкову фразу')
        # else:
        print(f'random_phrase random_phrase_entered: {random_phrase}')
        path = entry.get()  # користувач вводить текст
        print(f'entry random_phrase_entered: {path}')
        time2 = time.time()  # час завершення введення фрази користувачем
        print(f'time2: {time2}')

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

    #return time1, random_phrase, entry

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