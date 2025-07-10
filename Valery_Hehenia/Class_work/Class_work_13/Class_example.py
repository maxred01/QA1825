# #КЛАСС о объект
# class Car:
#     #Констркуктор (инициализатор)
#     def __init__(self, brand: str, color: str):
#         #Атрибуты объектов
#         self.brand = brand
#         self.color = color
#     #Методы объектов
#     def driver(self):
#         print(f'{self.brand} {self.color} is driving.')
#
# #Создание объектов
# ford = Car('Ford', 'red')
# tesla = Car('Tesla', 'blue')
#
# ford.driver()
# tesla.driver()
#
# #################################################################################
# #Наследование
# class Animal:
#     def __init__(self, name: str):
#         self.name = name
#
#     def speek(self):
#         print('Звук животного')
#
#
# class Dog(Animal):
#
#     def speek(self):
#         print('Гав')
#
#
# class Cat(Animal):
#
#     def speek(self):
#         print('Мяу')
#
# dog = Dog('bobik')
# cat = Cat('murzik')
#
# dog.speek()
# cat.speek()
#
# ###############################################################
#
# #Инкапсуляция
# class BankAccount:
#     def __init__(self, owner):
#         self.owner = owner
#         self.__balance = 0
#
#
#     def deposit(self, amount: float):
#         if amount > 0:
#             self.__balance += amount
#     def get_balance(self)-> float:
#         return self.__balance
#
#
# name_account = BankAccount('Valery')
# name_account.deposit(1000)
# print(name_account.get_balance())
#
#
# ###############################################################
#
# #Полиморфизм
# def animal_sound(animals: list[Animal]):
#     for animal in animals:
#         animal.speek()
#
# zoo = [Dog('bobik'), Cat('murzik')]
# animal_sound(zoo)
#
#
# ###############################################################

######Атрибуты######
class Dog:
    specis = "Собака"

    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Reks", 3)

print(my_dog.name)
print(my_dog.age)
print(my_dog.specis)

####Методы####
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    ## Обычный метод
    def area(self):
        return self.width * self.height

    ### Метод класса(раюотает с классом, а не с экземпляром)
    @classmethod
    def from_square(cls, side):
        return cls(side, side)###Создается квадрат

rect = Rectangle(4,5)
print(rect.area())

########Вызов класса
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
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14 * self._radius**2

circle = Circle(5)
print(circle.radius)

circle.radius = 10
print(circle.area)


