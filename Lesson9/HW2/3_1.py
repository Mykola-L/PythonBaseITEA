# на основі цього прикладу виконуємо практичні завдання
# the number of passengers in the cabin - кількість пасажирів у салоні - number_passengers_cabin

class Car: # створюємо клас автомобіль, заразервоване слово class, потім йде ім'я клусу, класи прийнято називати з великої букви

# конструктор який відповідає за ініціалізацію обєкта __init__ , два нижні підкреслення зліва і зправа від init
# конструктор це просто функція __init__ , яка буде викликатися в момент виклику класу.
    def __init__(self, model, engine_type, max_speed, color, number_passengers_cabin): # __init__(self):  це обовязковий елементк конструктора
# аргументи вказуються в довільному вигляді, ті які ми забажаємо, крім аргемента 1 = self, self має бути обов'язково
# визначаємо параметри якими ми хочемо охарактеризувати нащ автомобіль: model, engine_type - тип двигуна, , max_speed
# коли ми передали аргументи, ми маємо зберегти їх для нашого об'єкта
# ініціалізація цих аргументів проходить через ключове слово self
        self.model = model # аргемунет model приходить ззовні
        self.engine_type = engine_type
# self.engine_type це стосується одного об'єкта, engine_type - те що буде пердано в якості аргумента, це різні речі, хоча імена в них співпадають.
        self.max_speed = max_speed
        self.color = color
        self.number_passengers_cabin = number_passengers_cabin

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
        # self.move() # можемо викликати в середині класу метод move через self
        print(f'Max speed is {self.max_speed}')

    def color(self): #1 колір автомобіля
        print(f'The color of the car is {self.color}')

    def number_passengers_cabin(self): #2 кількість пасажирів у салоні
        print(f'There are {self.number_passengers_cabin} passengers in the cabin')


# конструктор і методи у class Truck можуть бути ті ж, але class Truck має додатковий метод
class Truck(Car): # в () ми передаємо ім'я класу від якого ми хочемо отримати всі його методи і атрибути

    def __init__(self, car_load, number_wheels):
        self.car_load = car_load
        self.number_wheels = number_wheels
# наш class Truck відрізняється від class Car, одним методом, все інше ми копіюємо.

# метод move буде вести себе інакше
    def move(self): # метод move в класі Truck і в класі Car веде себе по різному
        print('Truck is moving')

    def offload(self): # вивантажити вантаж автомобіля
        print('The items are being offloaded') # предмети вивантажуються

    def increment_speed(self, value):
        self.max_speed += value

    def car_load(self): #3 Car load - Вантажопідйомність автомобіля
        print('Car load capacity')

    def number_wheels(self): #4 кількість коліс автомобіля
        print('Number of car wheels')

car = Truck('MAN', 'V-12', 140, 'yellow', 1, 200)

car.move()
car.offload()
car.increment_speed(1)
car.get_max_speed()


car2 = Car('audi', 'v-6', 240, 'purple', 4, 6)
car2.move() # бере метод move з об'єкту Car - поліморфізм

print(car2.color)
print(car2.number_passengers_cabin)
# print(car.car_load)
# print(car.number_wheels)