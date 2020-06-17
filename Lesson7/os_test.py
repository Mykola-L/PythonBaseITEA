import os

print(os.getcwd()) # поточна робоча директорія

#print(os.listdir(r'C:\Users\Nick\AppData\Local\Programs')) # список файлів і директорій в папці

os.chdir('../Lesson6')
print(os.getcwd())