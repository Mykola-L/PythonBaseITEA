class Car: # створюємо клас автомобіль, заразервоване слово class, потім йде ім'я клусу, класи прийнято називати з великої букви

    def __init__(self, model, engine_type, max_speed, color, number_passengers_cabin):
        self.model = model
        self.engine_type = engine_type
        self.max_speed = max_speed
        self.color = color
        self.number_passengers_cabin = number_passengers_cabin

    def move(self):
        print(f'The car {self.model} is moving')

    def stop_engine(self):
        print(f'The car {self.model} has been stopped')

    def get_max_speed(self):
        print(f'Max speed is {self.max_speed}')

    def color(self): #1 колір автомобіля
        print(f'The color of the car is {self.color}')

    def number_passengers_cabin(self): #2 кількість пасажирів у салоні
        print(f'There are {self.number_passengers_cabin} passengers in the cabin')



class Truck(Car):

    def move(self):
        print('Truck is moving')

    def offload(self):
        print('The items are being offloaded')

    def increment_speed(self, value):
        self.max_speed += value

    def car_load(self): #3 Car load - Вантажопідйомність автомобіля
        print('Car load capacity 200 t')

    def number_wheels(self): #4 кількість коліс автомобіля
        print('Number of car wheels 6')

car = Truck('MAN', 'V-12', 140, 'yellow', 1)

car.move()
car.offload()
car.increment_speed(1)
car.get_max_speed()


car2 = Car('audi', 'v-6', 240, 'purple', 4)
car2.move()

print(car2.color)
print(car2.number_passengers_cabin)
print(car.color)
print(car.number_passengers_cabin)

car.car_load()
car.number_wheels()

