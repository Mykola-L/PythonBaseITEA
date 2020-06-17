from tkinter import Tk, Listbox, SINGLE, EXTENDED, END
root = Tk()
listbox = Listbox(root,height=5,width=15,selectmode=EXTENDED)
# entry це те що можна вводити, listbox це те, що можна дивитися, воно буде списком
list_of_countries = ["Ukraine", "Moldova", "Poland"] * 3
for country in list_of_countries:
    listbox.insert(END, country)
listbox.pack()
root.mainloop()

# вивидиться список країн 3 рази