from tkinter import Tk, Toplevel, Button, Label, Entry, END, Listbox, SINGLE
import random
import time
import datetime
import json

app_run_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
root = Tk()
label1 = Label(text='Для старту натисніть "Запуск гри"', font='Arial 20')
label2 = Label(text='', font='Arial 20')
entry = Entry(width=256)
count = 0

def clear_count():
    global count
    count = 0

def press_backspace(event):
    global count
    count = count + 1

def getRandomPhrase():
    file = open('list_random_phrases.txt', 'r')
    text = file.readlines()
    splitedText = [line.rstrip() for line in text]
    file.close()
    return random.choice(splitedText)

def save_in_file(speed):
    JSON_FILE_NAME = 'result_games.json'
    results = {
        'date': app_run_time,
        'speed': speed,
        'errors': count
        }

    data = json.load(open(JSON_FILE_NAME))

    if type(data) is dict:
        data = [data]

    data.append(results)
    with open(JSON_FILE_NAME, 'w') as outfile:
        json.dump(data, outfile)

def start_game():
    clear_count()
    startTime = time.time()
    random_phrase = getRandomPhrase()
    progress_label = 'Введіть текст випадкової фрази:'

    if (label1["text"] != progress_label):
        label1.config(text = progress_label)

    label2.config(text = random_phrase)

    entry.config(state='normal')
    entry.delete(0, END)

    entry.bind('<BackSpace>', press_backspace)

    def onKeyPressed(event):
        entered_text = entry.get()

        if str(random_phrase) == str(entered_text):
            entry.config(state = 'disabled')
            random_phrase_entered()

    entry.bind('<KeyRelease>', onKeyPressed)



    def random_phrase_entered():
        endTime = time.time()
        speed = endTime - startTime

        result_window = Toplevel(root)
        result_window.title('Ви ввели фразу вірно')
        result_window.label3 = Label(result_window, text='Ви ввели фразу вірно')
        result_window.label4 = Label(result_window, text=f'Швидкість набору тексту: {speed} с.')
        result_window.label5 = Label(result_window, text=f'Кількість виправлень: {count}')
        result_window.label3.pack()
        result_window.label4.pack()
        result_window.label5.pack()

        save_in_file(speed)

def show_history():
    history_window = Toplevel(root)
    history_window.title('Результат ігор')
    file_json = open('result_games.json', 'r')
    data = json.load(file_json)
    file_json.close()

    listbox = Listbox(history_window, height=50, width=150, selectmode=SINGLE)

    for i in data:
        row = f'Дата проходження: {i.get("date")}, Швидкість: {i.get("speed")}, Кількість помилок: {i.get("errors")}'
        listbox.insert(END, row)
    listbox.pack()

start_button = Button(root,
                text='Запуск гри',
                fg='black',
                bg='green',
                font='Arial 20',
                width=200,
                height=5,
                command=start_game
                )

history_button = Button(root,
                text='Перегляд історії ігор',
                fg='black',
                bg='orange',
                font='Arial 20',
                width=200,
                height=5,
                command=show_history
                )

root.title('Game')
root.geometry('1200x800')

start_button.pack()
history_button.pack()
label1.pack()
label2.pack()
entry.pack()

root.mainloop()