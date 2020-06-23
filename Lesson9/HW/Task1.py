class Rectangle:

    def __init__(self, height_rectangle, width_rectangle):
        self.height_rectangle = height_rectangle
        self.width_rectangle = width_rectangle

    def get_square(self):
        return self.height_rectangle * self.width_rectangle

    def get_perimeter(self):
        return self.height_rectangle * 2 + self.width_rectangle * 2

rectangle = Rectangle(10, 20)

print(f'Площа прямокутника {rectangle.get_square()} см.')
print(f'Периметр прямокутника {rectangle.get_perimeter()} см.')
print(f'Висота прямокутника {rectangle.height_rectangle} см., ширина прямокутника {rectangle.width_rectangle} см.')