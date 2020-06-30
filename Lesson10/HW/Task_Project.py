from tkinter import Tk, Toplevel, Button, Label, Entry, END, Listbox, SINGLE
import random
import time
import datetime
import json

a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

root = Tk()

def game_launch():
    time1 = time.time()
    file = open('list_random_phrases.txt', 'r')
    r = file.readlines()
    r2 = [line.rstrip() for line in r]
    random_phrase = random.choice(r2)
    file.close()

    entry = Entry(width=256)

    label1 = Label(text='Введіть текст випадкової фрази:', font='Arial 20')
    label2 = Label(text=f'{random_phrase}', font='Arial 20')
    label1.pack()
    label2.pack()
    entry.pack()

    def random_phrase_entered():
        path = entry.get()
        if str(random_phrase) == str(path):
            time2 = time.time()
            time3 = time2 - time1

            tl1 = Toplevel(root)
            tl1.title('Ви ввели фразу вірно')
            tl1.label3 = Label(tl1, text='Ви ввели фразу вірно')
            tl1.label4 = Label(tl1, text=f'Швидкість набору тексту: {time3} с.')
            tl1.label3.pack()
            tl1.label4.pack()

            JSON_FILE_NAME = 'result_games.json'

            my_obj = {'Date and time of the game': a3,
                      'Typing speed seconds': time3
                      }

            file_json = open(JSON_FILE_NAME, 'a')
            json.dump(my_obj, file_json, indent="")
            file_json.close()

        else:
            list_1 = list(random_phrase)
            list_2 = list(path)
            sum(a != b for a, b in zip(list_1, list_2))
            abs(len(list_1) - len(list_2))

            difference = sum(a != b for a, b in zip(list_1, list_2))
            difference += abs(len(list_1) - len(list_2))

            tl3 = Toplevel(root)
            tl3.title('Ви ввели невірну випадкову фразу.')
            tl3.label5 = Label(tl3, text='Ви ввели невірну випадкову фразу.')
            tl3.label6 = Label(tl3, text=f'Кількість помилок: {difference}')
            tl3.label5.pack()
            tl3.label6.pack()

    button3 = Button(root,
                     text='Випадкову фразу введено',
                     fg='black',
                     bg='yellow',
                     font='Arial 20',
                     width=200,
                     height=5,
                     command=random_phrase_entered
                     )

    button3.pack()

def result_games():
    tl2 = Toplevel(root)
    tl2.title('Результат ігор')

    file_json = open('result_games.json', 'r')
    res = json.load(file_json)
    file_json.close()

    values_list = []
    for i in res.items():
        values_list.append(i)

    listbox = Listbox(tl2, height=50, width=150, selectmode=SINGLE)
    list_of_files = list(values_list)
    for i  in list_of_files:
        listbox.insert(END, i)
    listbox.pack()

button1 = Button(root,
                text='Запуск гри',
                fg='black',
                bg='green',
                font='Arial 20',
                width=200,
                height=5,
                command=game_launch
                )

button2 = Button(root,
                text='Перегляд історії ігор',
                fg='black',
                bg='orange',
                font='Arial 20',
                width=200,
                height=5,
                command=result_games
                )

root.title('Game')
root.geometry('1200x800')

button1.pack()
button2.pack()

root.mainloop()