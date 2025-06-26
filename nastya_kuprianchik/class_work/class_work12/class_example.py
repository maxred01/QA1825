#класс и объект
class Car:
    #иницилизация (конструктор)
    def __init__(self, brand: str, color: str):
        #атрибуты
        self.brand = brand
        self.color = color
        #методы
    def drive(self):
        print(f'{self.brand} {self.color}')
#создание объекта
bmw = Car('BMW', ' синий')
tesla = Car('TESLA', 'red')

bmw.drive()
tesla.drive()
############################################################

#наследование
class Animal:
    def __init__(self, name: str):
        self.name = name
    def speak(self):
        print('звук животного')

class Dog(Animal):#наследует от Animal
    def speak(self):#преопределяет метод
        print('гав')

class Cat(Animal):
    def speak(self):
        print('mou')

dog = Dog('Боб')
cat =Cat('murka')

dog.speak()
cat.speak()
##################################################
#Инкапсуляция
class BankAccount:
    def __init__ (self, ower: str):
        self.ower = ower
        self.__balance = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
    def get_balance(self) -> float:
        return self.__balance

name_account = BankAccount('nastya')
name_account.deposit(10000)
print(name_account.get_balance())
######################################################

#Полиморфиз
def animals_sound(animals: list[Animal]):
    for animals in animals:
        animals.speak()

zoo = [Dog('Боб'), Cat('murka')]
animals_sound(zoo)
#############################################

from abc import ABC, abstractmethod

class Shape(ABC):
    def areal(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def areal(self) -> float:
        return 3.14 + self.radius ** 2
#Инкапсуляция (Защита дфнных)
#Наследование (ПЕреиспользование данных
#Полиморфиз (гибкость интерфейса)
#Абстракция (упрощение)
#########################################
class Book:
    def __init__(self, title: str, autor: str):
        self.title = title
        self.autor = autor

    def __info__(self):
        print(f"Книга: {self.title}, Автор: {self.autor}")

book = Book("Гарри Поттер","Дж. Роулинг")
book.__info__()

##########################
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

student = Student('Anna')
student.add_grade(5)
student.add_grade(4)
print(student.grades)
#########################################

class PasswordManager:
    def set_password(self, pwd: str):
        if len(pwd) > 8:
            self.__password = pwd

    def check_password(self, pwd: str):
        return self.__password == pwd

    def check_password(self, pwd: str):
        return self.__password == pwd

pm = PasswordManager()
pm.set_password('security123')
print(pm.check_password('security123'))
################################
class Vehocle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year
    def __info__(self):
        print(f'Марка:{self.brand}, Год: {self.year}')


class ElectricCar(Vehocle):
    def __init__(self, brand: str, year:int, battery_capacity:float):
        super().__init__(brand, year)
        self.battery_capacity = battery_capacity

    def __info__(self):
        print(f'{self.brand} {self.year} {self.battery_capacity}')

car = ElectricCar("Tesla", 2023, 75)
car.info()  # "Марка: Tesla, Год: 2023, Батарея: 75 kWh"
####################################################
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 1)


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


def print_area(shape):
    if isinstance(shape, Circle):
        print(f"Площадь круга: {shape.area()}")
    elif isinstance(shape, Square):
        print(f"Площадь квадрата: {shape.area()}")
    else:
        print("Неизвестная фигура")


# Пример использования
circle = Circle(radius=5)
square = Square(side=4)
print_area(circle)
print_area(square)

