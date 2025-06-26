#Класс и объект
class Car:
    #Конструктор (инициализатор)
    def __init__(self, brand: str, color: str):
        #Атрибуты объектов
        self.brand = brand
        self.color = color

    #Методы объектов
    def driver(self):
        print(f"{self.brand} {self.color} едет")

#Создание объектов
bmw = Car("BMW", "синяя")
tesla = Car("Tesla", "черная")

bmw.driver()
tesla.driver()


#Наследование (Переиспользование кода)
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        print("Звук животного")

class Dog(Animal): #наследуется от Animal
    def speak(self): #переопределение методов
        print("Гав")

class Cat(Animal): #наследуется от Animal
    def speak(self): #переопределение методов
        print("Мяу")

dog = Dog("Бобик")
cat = Cat("Мурка")

dog.speak()
cat.speak()


#Инкапсуляция (Защита данных)
class BankAccount:
    def __init__(self, owner: str):
        self.owner = owner
        self.__balance = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance

name_account = BankAccount("Максим")
name_account.deposit(1000)
print(name_account.get_balance())


#Полиморфизм (Гибкость интерфейса)
def animal_sound(animals: list[Animal]):
    for animal in animals:
        animal.speak()

zoo = [Dog("Бобик"), Cat("Мурка")]
animal_sound(zoo)


#Абстракция (Упрощение сложного)

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def areal(self) -> float:
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius: float):
#         self.radius = radius
#
#     def area(self) -> float:
#         return 3.14 * self.radius ** 2
#
# circle = Circle(5)
# print(circle.area)


# Создайте класс Book, который хранит название книги (`title`) и автора (`author`).
# Добавьте метод info(), который печатает: "Книга: {название}, Автор: {автор}".
# Пример использования:
# book = Book("Гарри Поттер", "Дж. Роулинг")
# book.info()  # Книга: Гарри Поттер, Автор: Дж. Роулинг

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def info(self):
        print (f"Книга: {self.title}, Автор: {self.author}")

book = Book("Гарри Поттер", "Дж. Роулинг")
book.info()

# Создайте класс Student с атрибутами name (имя) и grades (список оценок).
# Добавьте метод add_grade(grade), который добавляет оценку в список.
# Пример:
# student = Student("Анна")
# student.add_grade(5)
# student.add_grade(4)
# print(student.grades)  # [5, 4]

class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []
    def add_grade(self, grade: int):
        self.grades.append(grade)

student = Student("Анна")
student.add_grade(5)
student.add_grade(4)
print (student.grades)

#Создайте класс PasswordManager с приватным атрибутом __password. Добавьте методы:
# - set_password(pwd) — устанавливает пароль, если его длина >= 8 символов,
# - check_password(pwd) — проверяет, совпадает ли переданный пароль с сохранённым.
# Пример:
# pm = PasswordManager()
# pm.set_password("qwerty")  # Не установится (слишком короткий)
# pm.set_password("secure123")
# print(pm.check_password("secure123"))  # True

class PasswordManager:
    def __init__(self):
        self.__password = None

    def set_password(self, password: str):
        if len (password) >= 8:
            self.__password = password

    def check_password(self, password: str) -> bool:
        return self.__password == password

pm = PasswordManager()
pm.set_password("qwerty")  # Не установится (слишком короткий)
pm.set_password("secure123")
print(pm.check_password("secure123")) # True

# Создайте класс Vehicle с атрибутами brand и year, и методом info() (печатает бренд и год).
# Создайте подкласс ElectricCar, который добавляет атрибут battery_capacity.
# Пример:
# car = ElectricCar("Tesla", 2023, 75)
# car.info()  # "Марка: Tesla, Год: 2023, Батарея: 75 kWh"

class Vehicle:
    def __init__(self, brand: str, year: str):
        self.brand = brand
        self.year = year
    def info(self):
        print(f"Марка: {self.brand}, Год: {self.year}")

class ElectricCar(Vehicle):
    def __init__(self, brand: str, year: int, battery_capacity: int):
        super().__init__(brand, year)
        self.battery_capacity = battery_capacity

    def info(self):
        super().info()
        print(f"Батарея: {self.battery_capacity} kWh")


car = ElectricCar("Tesla", 2023, 75)
car.info()  # "Марка: Tesla, Год: 2023, Батарея: 75 kWh"


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
        return 3.14 * (self.radius ** 2)


class Square:
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

def print_area (shape):
    print(f'Площадь: {shape.area()}')

circle = Circle(radius=5)
square = Square(side=4)
print_area(circle)
print_area(square)

