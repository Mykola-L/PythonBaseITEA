import requests

image_list = ['https://images.freeimages.com/images/small-previews/5c6/sunset-jungle-1383333.jpg']

for idx, file in enumerate(image_list):
    response = requests.get('https://images.freeimages.com/images/small-previews/5c6/sunset-jungle-1383333.jpg')
# response.content # content - це бінарні дані цього файлу
# записуємо в файл малюнок, закриваємо файл.
    with open(f'{file.split("/")[-1]}', 'wb') as image:
        image.write(response.content)

# якщо ми працюємо з не текстовими даними, і хочемо записати ці дані, ми маємо додати букву b в режим записування: 'wb'
# write binary - записати бінарні дані
