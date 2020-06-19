import datetime
import json

# визначає час
a3 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(a3)

try:
    b1 = str(input("Введіть інформацію про контакт: ім'я ")) # label1
    b2 = str(input("Введіть інформацію про контакт: прізвище "))
    b3 = int(input("Введіть інформацію про контакт: номер телефону "))
    b4 = str(input("Введіть інформацію про контакт: адресу "))
    b5 = str(input("Зберегти контакт? Можлива відповідь: Так, Ні. "))
except:
    print('Ви ввели невірні дані')

if b5 == 'Так':

    JSON_FILE_NAME = 'my_contacts.json'

# my_obj = {"Введіть інформацію про контакт: ім'я ": b1,
#           "Введіть інформацію про контакт: прізвище ": b2,
#           "Введіть інформацію про контакт: номер телефону ": b3,
#           "Введіть інформацію про контакт: адресу ": b4
#           } # створюю об'єкт

    my_obj = {'Contact creation time': a3,
            'Name': b1,
          'Surname': b2,
          'Phone number': b3,
          'Address': b4
          } # створюю об'єкт


    file_json = open(JSON_FILE_NAME, 'a')
    json.dump(my_obj, file_json) # метод json.dump серіалізує об'єкт в файл, записує дані не у змінну а у файл.
    file_json.close()




try:
    b6 = str(input("Показати всі доступні контакти? Можлива відповідь: Так, Ні. "))
except:
    print('Ви ввели невірні дані')

if b6 == 'Так':
    file_json = open('my_contacts.json', 'r')  # 'r' файл відкритий на читання
    res = json.load(file_json)  # метод json.load десеріалізує об'єкт з файлу, бере дані з файлу і записує в словник
    file_json.close()
    print(res)

try:
    b7 = str(input("Очистити список контактів? Можлива відповідь: Так, Ні. "))
except:
    print('Ви ввели невірні дані')

if b7 == 'Так':
    open('my_contacts.json', 'w').close()  # очищуємо файл