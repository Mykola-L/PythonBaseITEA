import os

file_path = r'E:\PyCharm\PythonBaseITEA\Lesson7\path_examp.py'
# роблю копію повного шляху до поточного файлу, на файл права кнопка мишки - Copy - Copy Path...


file_name = os.path.basename(file_path)

# поверне ім'я шляху, і виключить з нього ім'я файлу
dir_path = os.path.dirname(file_path)

print(os.path.join(file_name, dir_path)) # об'єднає шлях до файла і ім'я файла

#print(os.path.exists(file_path)) # перевіряє чи існує шлях

# print(os.path.isdir(file_path)) # перевіряє є шлях директорією – папкою

#print(os.path.isfile(file_path)) # перевіряє є шлях файлом

print(os.path.split(file_path))