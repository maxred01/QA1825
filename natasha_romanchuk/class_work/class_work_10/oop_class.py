

# КЛАСС И ОБЬЕКТ
class Car:
    # (инициализация)    Конструктор
    def __init__(self,brand: str, color: str) -> None:
    # Атрибуты обьектов
        self.brand = brand
        self.color = color

    # Методы обьектов
    def driver(self):
        print(f'{self.brand} {self.color} едет')


# Создание обьектов
bmv = Car('BMV','синяя')
tesla = Car('Tesla','черная')

bmv.driver()
tesla.driver()

#############################################################################################################


#  Наследование
class Animal:
    def __init__(self,name: str) -> None:
        self.name = name

    def speak(self):
        print('Звук животного')

class Dog(Animal):         # наследуется от Animal
    def speak(self):       # переопределение методов
        print('Гав')

class Cat(Animal):          # наследуется от Animal
        def speak(self):    # переопределение методов
            print('Мяу')

dog = Dog('Боббик')
cat = Cat('Мурка')

dog.speak()
cat.speak()

#############################################################################################################

# Инкасуляция
class BankAccount:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.__balance = 0

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance

name_account = BankAccount('Максим')
name_account.deposit(1000)
print(name_account.get_balance())


#############################################################################################################


# Полиморфизм
def animal_sound(animals: list[Animal]) -> None:
    for animal in animals:
        animal.speak()

zoo = [Dog('Боббик'), Cat('Мурка')]
animal_sound(zoo)


#############################################################################################################


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) ->float:
        return 3.14 + self.radius ** 2

circle = Circle(5)
print(circle.area())


# Инкапсуляция (Защита данных)
# Наследование (Переиспользование кода)
# Полиморфизм (Гибкость интерфейса)
# Абстракция (Упрощение сложного)


#############################################################################################################
# Задача 1
# Создайте класс Book, который хранит название книги (`title`) и автора (`author`). Добавьте метод info(), который печатает: "Книга: {название}, Автор: {автор}".
# Пример использования:
#
# book = Book("Гарри Поттер", "Дж. Роулинг")
# book.info()  # Книга: Гарри Поттер, Автор: Дж. Роулинг

class Book():
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
    def info(self):
        print(f'Книга:"{self.title}", Автор: "{self.author}"')

book = Book("Гарри Поттер", "Дж. Роулинг")
book.info()

# Задача 2
# Создайте класс Student с атрибутами name (имя) и grades (список оценок). Добавьте метод add_grade(grade), который добавляет оценку в список.
# Пример:
# student = Student("Анна")
# student.add_grade(5)
# student.add_grade(4)
# print(student.grades)  # [5, 4]

class Student():
    def __init__(self, name: str) -> None:
        self.name = name
        self.grades = []

    def add_grade(self, grade: int) -> None:
        self.grades.append(grade)

student = Student("Анна")
student.add_grade(5)
student.add_grade(4)
print(student.grades)  # [5, 4]

######  АТРИБУТЫ ####################################################
class Dog:
    specils = 'Собака'

    def __init__(self, name,age)-> None:
        self.name = name
        self.age = age

my_dog = Dog('Rex',3)
print(my_dog.name)
print(my_dog.age)
print(my_dog.specils)


#######  МЕТОДЫ  ####################################################
class Rectangle :
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    # Обычный метод
    def area(self):
        return self.width * self.height

    # Метод класса
    @classmethod
    def from_area(cls,side):
        return cls(side, side)     # Создаст квадрат

rect = Rectangle(4,5)
print(rect.area())

### Вызов метода класса
square = Rectangle.from_area(4)
print(square.area())


#######  СВОЙСТВА  ####################################################
class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value):
        if value < 0:
            raise ValueError('Радиус не может быть отрицательным')

    @property
    def area(self):
        return 3.14 * self._radius ** 2

    circle = Circle(5)
    print(circle.radius)

    circle.radius = 10

    print(circle.area)
