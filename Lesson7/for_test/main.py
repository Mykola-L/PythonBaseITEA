# Розв'яжемо задачу, яка буде очищати поточну директорію
import os
import random

def seed_direcory(number_of_files, ext):
    # функція створює декілька файлів, доповнить нашу директорію якимось файлами

    #for i in range(number_of_files): # змінну і можна змінити на _ це анонімна змінна, до якої не можливо звернутися.
    # до змінної _ звернутися можна, але в цьому немає сенсу її записати неможливо в інший об'єкт або щке кудись.
    for _ in range(number_of_files):
        open(f'{random.randint(0, 1000)}.{ext}', 'w').close()

# функція буде повністю очищати директорію папку крім файлу main з якого ми запускаємо програму
def clean_directory(directory_path='.', exclude_filename='main.py'):
    files = os.listdir(directory_path)

    # for file in files:
    #
    #     if file != exclude_filename:
    #         os.remove(file)


    for file in set(files) - set(exclude_filename): # конструкція без if

            os.remove(file)


# seed_direcory(4, 'txt') # створюємо 4 текстові файли з випадковими текстовими значеннями

clean_directory()
