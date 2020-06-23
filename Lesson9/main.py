class Car: # створюємо клас автомобіль, заразервоване слово class, потім йде ім'я клусу, класи прийнято називати з великої букви

# конструктор який відповідає за ініціалізацію обєкта __init__ , два нижні підкреслення зліва і зправа від init
# конструктор це просто функція __init__ , яка буде викликатися в момент виклику класу.
    def __init__(self, model, engine_type, max_speed): # __init__(self):  це обовязковий елементк конструктора
# аргументи вказуються в довільному вигляді, ті які ми забажаємо, крім аргемента 1 = self, self має бути обов'язково
# визначаємо параметри якими ми хочемо охарактеризувати нащ автомобіль: model, engine_type - тип двигуна, , max_speed
# коли ми передали аргументи, ми маємо зберегти їх для нашого об'єкта
# ініціалізація цих аргументів проходить через ключове слово self
        self.model = model # аргемунет model приходить ззовні
        self.engine_type = engine_type
# self.engine_type це стосується одного об'єкта, engine_type - те що буде пердано в якості аргумента, це різні речі, хоча імена в них співпадають.
        self.max_speed = max_speed
# ми визначили три атрибути обєкта: self.model , self.engine_type , self.max_speed , хоча об'єкт ще не створили
# те що ми вказуємо через self називається атрибут об'єкта, або змінна об'єкта
# змінну об'єкта ми визначили, тепер можемо створювати автомобіль
# визначимо методи, метод це функція яка приймає аргементи
# Метод — функция объекта, принимающая в качестве первого обязательного аргумента
# ссылку на объект - self

# кожен метод класу відділяється одним Tab
# визначимо метод всередині класу Car
    def move(self): # метод їхати
        print(f'The car {self.model} is moving')

    def stop_engine(self): # метод зупинити мотор
        print(f'The car {self.model} has been stopped')

    def get_max_speed(self):
        print(f'Max speed is {self.max_speed}')

# ми створили самостійно клас, такий же як і будь-який інший клас в Python, як будь-який інший тип даних ми створили свій тип даних а саме свій клас.

# ім'я змінної має відрізнятися від імені класу
# в даномуу випадку ім'я змінної з малої букви, ім'я класу з великої букви
# створюємо змінну, аписую в не ї клас Car
# конструктор __init__ може приймати як позиційні аргументи, так і ключові
# в нас всі аргументи позиційні, ми їх передаємо в тому ж порядку
# в Python не можливо обмежити модуль так щоб він приймав тільки один тип даних, наприклад рядок
# в Python динамічна типізація, змінні можуть змінювати тип під час виконання програми
# в Python змінна може бути рядком, потім перетворитися в int, потім в спискок
car = Car('audi', 'v-6', 240) # викликаємо метод car
# ми маємо об'єкт car, тепер ми може працювати з цим об'єктом як і з іншими будь-якими об'єктами.

car.move() # у car викличемо метод move(), вказуємо з викликом, так як методи мають викликатися
# так як вказано self ми ніяких аргументів не передаємо в цю функції
# self вказаний всередині класу не зобов'язує нас з зовнішнього коду передавати якийсь аргумент, автоматично замість нас цей self буде переданий.

# У нашого об'єкта car був успішно викликаний метод move, хоча метод move нічого не повертає, і ніяких даних в іншу змінну ми не записували

car.stop_engine()
# До об’єктів ми можемо звертатися ззовні і змінювати їхній стан.
# так я можу звертатися до змінних об’єкта з зовнішнього коду, з за меж класу
car.max_speed += 20 # збільшуємо швидкість на 20
car.get_max_speed()

print(car.model, car.engine_type, car.max_speed)
print('*' * 10) # 10 зірочок виведе

# ми можемо сворювати в нашій програмі декілька об'єктів

car2 = Car('bmw', 'v-8', 260)

car2.move()
car2.stop_engine()
car2.get_max_speed()
print(car2.model, car2.engine_type, car2.max_speed)