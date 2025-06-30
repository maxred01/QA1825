# КЛАСС И ОБЪЕКТ
class Car:
    # Конструктор(инициализатор)
    def __init__(self, brand: str, color: str):
        #Атрибуты объектов
        self.brand = brand
        self.color = color

    # методы объектов
    def driver(self):
        print(f"{self.brand} {self.color} едет")

# Создание объектов
dmw = Car  ("BMW", "синяя")
tesla = Car("Tesla", "черная")


dmw.driver()
tesla.driver()


################################################################################

# наследование
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        print("Звук животного")


class Dog(Animal): # Наследуется от Animal
    def speak(self): # переопределение методов
        print("Гав")


class Cat(Animal):  # Наследуется от Animal
    def speak(self):  # переопределение методов
        print("Мяу")

dog = Dog("Бобик")
cat = Cat("Мурка")

dog.speak()
cat.speak()

################################################################################

# Инкапсуляция
class BankAccount:
    def __init__(self, owner: str):
        self.owner = owner
        self.__balance = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self)-> float:
        return self.__balance


name_account = BankAccount("Максим")
name_account.deposit(1000)
print(name_account.get_balance())

################################################################################

# Полиморфизм
def animal_sound(animals: list[Animal]):
    for animal in animals:
        animal.speak()

zoo = [Dog("Бобик"), Cat("Мурка")]

animal_sound(zoo)


################################################################################


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 + self.radius ** 2


circle = Circle(5)
print(circle.area())

# Инкапсуляция (Защита данных)
# Наследование (Переиспользование кода)
# Полиморфизм (Гибкость интерфейса)

################################################################################

# Задача №1
class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}")


book = Book("Гарри Поттер", "Дж. Роулинг")
book.info()

# Задача №2

class Student:

    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, grade:int):
        self.grades.append(grade)


student = Student("Анна")
student.add_grade(5)
student.add_grade(4)
print(student.grades)

# Задача 3

class PasswordManager:
    def __init__(self):
        self.__password = None

    def set_password(self, pwd: str):
        if len(pwd) >= 8:
            self.__password = pwd

    def check_password(self, pwd: str) -> bool:
        return self.__password == pwd


pm = PasswordManager()
pm.set_password("qwerty")  # Не установится (слишком короткий)
pm.set_password("secure123")
print(pm.check_password("secure123"))  # True

# Задача 4

# Создайте класс Vehicle с атрибутами brand и year, и методом info() (печатает бренд и год).
# Создайте подкласс ElectricCar, который добавляет атрибут battery_capacity.
# Пример:
# car = ElectricCar("Tesla", 2023, 75)
# car.info()  # "Марка: Tesla, Год: 2023, Батарея: 75 kWh"

# class Vehicle:
#     def __init__(self, brand: str, year: int):
#         self.brand = brand
#         self.year = year
#
#     class info(ElectricCar):
#         def speak(self):
#             print(f"м=Марка: {self.brand}, Год: {self.year})
#
# class ElectricCar(Vehicle):
#         def __init__(self, battery_capacity: int):
#         super () __init__()
#         print(f"Бытарея: {}")
#
# car = ElectricCar("Tesla", 2023, 75)
# car.info()  # "Марка: Tesla, Год: 2023, Батарея: 75 kWh"

# Создайте классы Circle и Square с методом area().
# Напишите функцию print_area(shape), которая вызывает area() у переданного объекта.
# Пример:
# circle = Circle(radius=5)
# square = Square(side=4)
# print_area(circle)  # Площадь круга: 78.5
# print_area(square)  # Площадь квадрата: 16

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

class Square:
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

def print_area(shape):
    print(f"Площадь: {shape.area}")


circle = Circle(radius=5)
square = Square(side=4)
print_area(circle)  # Площадь круга: 78.5
print_area(square)  # Площадь квадрата: 16