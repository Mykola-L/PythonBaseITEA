from tkinter import Tk, Button, Label, Entry
import requests

root = Tk()

label1 = Label(text='Введіть посилання на файл в інтернеті')
label2 = Label(text='Введіть шлях, за яким файл буде збережений на пристрій')
label3 = Label(text="Введіть ім'я і формат файлу")
entry1 = Entry(width=256)
entry2 = Entry(width=256)
entry3 = Entry(width=256)

def save_file():

    r = requests.get(entry1.get())
    path2 = entry2.get()
    path3 = entry3.get()

    if path2 != '':
        a = path2
    else:
        a = './'

    if path3 != '':
        b = path3
    else:
        s = entry1.get()
        b = (s.split("/")[-1])

    with open(f'{a}{b}', 'wb') as file:
        file.write(r.content)

button = Button(root,
                text='Зберегти введені дані!',
                fg='red',
                bg='green',
                width=600,
                height=10,
                command=save_file)

root.geometry('600x400')

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
button.pack()

root.mainloop()
