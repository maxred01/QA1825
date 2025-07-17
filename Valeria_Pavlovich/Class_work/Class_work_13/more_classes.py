class Dog:
    species = 'Dog'

    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog('Rex', 3)
print(my_dog.species)
print(my_dog.name)
print(my_dog.age)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @classmethod
    def from_square(cls, side):
        return cls(side, side)

rect = Rectangle(4, 5)
print(rect.area())

square = Rectangle.from_square(4)
print(square.area())

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')

    @property
    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(5)
print(circle.radius)

circle.radius = 10
print(circle.area)