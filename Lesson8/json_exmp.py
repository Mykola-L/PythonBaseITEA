# словник перетворюю в об'єкт типу json
# import json

# my_obj = {'title': 30, 'price': 100, 'quantity': 20} # створюю об'єкт
#
# print(type(my_obj)) # функція type(), приймає на вхід змінну і виводить на екран тип об'єкта
# print(my_obj)
# result = json.dumps(my_obj) # метод json.dumps() переводить Python об'єкт до json об'єкту
#
# print(type(result))
# print(result[::]) # можу звернутися до рядка по індексу

# qwe = '{"title": 30, "price": 100, "quantity": 20}' # рядок строка
#
# result = json.loads(qwe) # перетворюємо json в словник
#
# print(result['title'])

# import json
#
# JSON_FILE_NAME = 'data.json'
#
# my_obj = {'title': 30, 'price': 100, 'quantity': 20} # створюю об'єкт
#
# file_json = open(JSON_FILE_NAME, 'r') # 'r' файл відкритий на читання
# res = json.load(file_json) # метод json.dump десеріалізує об'єкт з файлу, безе дані з файлу і записує в словник
# file_json.close()
# print(res)

import json
# дві функції json
import json
JSON_FILE_NAME = 'data.json'

my_obj = {'title': 30, 'price': 100, 'quantity': 20} # створюю об'єкт

def write_to_json_file():
    file_json = open(JSON_FILE_NAME, 'a')
    json.dump(my_obj, file_json) # метод json.dump десеріалізує об'єкт з файлу, безе дані з файлу і записує в словник
    file_json.close()

def read_from_json_file():
    file_json = open(JSON_FILE_NAME, 'r') # 'r' файл відкритий на читання
    res = json.load(file_json) # метод json.load десеріалізує об'єкт з файлу, безе дані з файлу і записує в словник
    file_json.close()
    print(res)