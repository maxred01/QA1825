class Car:
    def __init__(self, brand: str, color: str):
        self.brand = brand
        self.color = color

    def driver(self):
        print(f'{self.color} {self.brand} arrives')


bmw = Car('BMW', 'Blue')
tesla = Car('Tesla', 'Black')

bmw.driver()
tesla.driver()

#####################################################

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        print('Animal sound')

class Dog(Animal):

    def speak(self):
        print('Woof')

class Cat(Animal):
    def speak(self):
        print('Meow')

dog = Dog('Bob')
cat = Cat('Tom')

dog.speak()
cat.speak()

#####################################################
class BankAccount:
    def __init__(self, owner: str):
        self.owner = owner
        self.__balance = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance

name_account = BankAccount('John')
name_account.deposit(1000)
print(name_account.get_balance())
#####################################################
def animal_sound(animals: list[Animal]):
    for animal in animals:
        animal.speak()

zoo = [Dog('Bob'), Cat('Tom')]

animal_sound(zoo)
#####################################################
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def areal(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 + self.radius ** 2

circle = Circle(5)
print(circle.area())
