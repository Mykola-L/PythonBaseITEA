class Rectangle: # клас прямокутник

# конструктор
    def __init__(self, height_rectangle, width_rectangle):
# height_rectangle - висота прямокутника
# width_rectangle - ширина прямокутника
# area_rectangle - площа прямокутника
# perimeter_rectangle - периметр прямокутника
        self.height_rectangle = height_rectangle # height_rectangle - висота прямокутника
        self.width_rectangle = width_rectangle # width_rectangle - ширина прямокутника

# замінив назви функцій
    def get_square(self): # area_rectangle - площа прямокутника
        return self.height_rectangle * self.width_rectangle

    def get_perimeter(self): # perimeter_rectangle - периметр прямокутника
        return self.height_rectangle * 2 + self.width_rectangle * 2

rectangle = Rectangle(10, 20)

# rectangle.area_rectangle() # викликаємо функцію конструктора
# rectangle.perimeter_rectangle() # викликаємо функцію конструктора
#
# print(rectangle.area_rectangle()) # виводимо на друк функцію конструктора, можливо об'єкт
# print(rectangle.perimeter_rectangle()) # виводимо на друк функцію конструктора, можливо об'єкт

print(f'Площа прямокутника {rectangle.get_square()} см.')
print(f'Периметр прямокутника {rectangle.get_perimeter()} см.')
print(f'Висота прямокутника {rectangle.height_rectangle} см., ширина прямокутника {rectangle.width_rectangle} см.')