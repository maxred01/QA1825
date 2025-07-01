# КЛАСС И ОБЪЕКТ
class Car:
    # Конструктор (инициализатор)
    def __init__(self, brand: str, color: str):
        #  Атрибуты объектов
        self.brand = brand
        self.color = color

    # Методы объектов
    def driver(self):
        print(f"{self.brand} {self.color} едет")


# Создание объектов
dmw = Car("BMW", "синяя")
tesla = Car("Tesla", "черная")


dmw.driver()
tesla.driver()

#####################################################################################

# Наследованеи
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        print("Звук животного")


class Dog(Animal):  # наследуется от Animal
    def speak(self):  # переопределение методов
        print("Гав")


class Cat(Animal):  # наследуется от Animal
    def speak(self):  # переопределение методов
        print("Мяу")


dog = Dog("бобик")
cat = Cat("мурка")

dog.speak()
cat.speak()

#####################################################################################

# Полиморфизм
def animal_sound(animals: list[Animal]):
    for animal in animals:
        animal.speak()

zoo = [Dog('бобик'), Cat('мурка')]

animal_sound(zoo)

#####################################################################################

# Инкапусуляция
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

#####################################################################################


# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def areal(self) -> float:
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius: float):
#         self.radius = radius
#
#     def area(self) -> float:
#         return 3.14 + self.radius ** 2
#
#
# circle = Circle(5)
# print(circle.area())

# Инкапсуляция (Защита данных)
# Наследование (Переиспользование кода)
# Полиморфизм (Гибкость интерфейса)
# Абстракция (Упрощение сложности/сложного)


# Создайте класс Student с атрибутами name (имя) и grades (список оценок). Добавьте метод add_grade(grade), который добавляет оценку в список.
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
print(student.grades)




# Создайте класс PasswordManager с приватным атрибутом __password. Добавьте методы:
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

    def set_password(self, pwd: str):
        if len(pwd) >= 8:
            self.__password = pwd

    def check_password(self, pwd: str) -> bool:
        return self.__password == pwd


pm = PasswordManager()
pm.set_password("qwerty")  # Не установится (слишком короткий)
pm.set_password("secure123")
print(pm.check_password("secure123"))  # True


# Создайте класс Vehicle с атрибутами brand и year, и методом info() (печатает бренд и год). Создайте подкласс ElectricCar, который добавляет атрибут battery_capacity.
# Пример:
# car = ElectricCar("Tesla", 2023, 75)
# car.info()  # "Марка: Tesla, Год: 2023, Батарея: 75 kWh"

class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"Марка: {self.brand}, Год: {self.year}")


class ElecticCar(Vehicle):
    def __init__(self, brand: str, year: int, battery_capacity: int):
        super().__init__(brand, year)
        self.battery_capacity = battery_capacity

    def info(self):
        super().info()
        print(f"БатареяЖ {self.battery_capacity} kWh")


car = ElecticCar("Тесла", 2023, 75)
car.info()


# Создайте классы Circle и Square с методом area(). Напишите функцию print_area(shape), которая вызывает area() у переданного объекта.
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
    print(f"Площадь: {shape.area()}")

circle = Circle(radius=5)
square = Square(side=4)
print_area(circle)  # Площадь круга: 78.5
print_area(square)  # Площадь квадрата: 16


# Атрибуты
class Dog:
    specis = "Собака"

    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Rex", 3)

print(my_dog.name)
print(my_dog.age)
print(my_dog.specis)


# Методы
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Обычный метод
    def area(self):
        return self.width * self.height

    # Метод класса (работает с классом, а не экземпляром)
    @classmethod
    def from_square(cls, side):
        return cls(side, side)  # Создоваться квадрат


rect = Rectangle(4, 5)
print(rect.area())

# Вызов метода класс
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
            raise ValueError("Радиус не может быть отрицательным")

    @property
    def area(self):
        return 3.14 * self._radius ** 2


circle = Circle(5)
print(circle.radius)

circle.radius = 10

print(circle.area)


"0123456789"[6] = 7
"0123456789"[6] == "7"

