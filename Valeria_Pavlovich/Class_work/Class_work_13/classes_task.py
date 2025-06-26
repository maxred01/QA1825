# class Book:
#     def __init__(self, title: str, author: str):
#         self.title = title
#         self.author = author
#
#     def book_info(self):
#         print(f'Book: {self.title}, Author: {self.author}')
#
#
# hp = Book('Harry Potter', 'J. K. Rowling')
#
# hp.book_info()
##################################################################
# class Student:
#     def __init__(self, name: str):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade: int):
#         self.grades.append(grade)
#
# student = Student('Anna')
# student.add_grade(5)
# student.add_grade(4)
# print(student.grades)
# ####################################################
#
# class PasswordManager:
#     def __init__(self):
#         self.__password = None
#
#     def set_password(self, pwd:str):
#         if len(pwd) >= 8:
#             self.__password = pwd
#
#     def check_password(self, pwd: str) -> bool:
#         return self.__password == pwd
#
# pm = PasswordManager()
# pm.set_password('qwerty')
# pm.set_password('secure123')
# print(pm.check_password("secure123"))
# ####################################################
# class Vehicle:
#     def __init__(self, brand: str, year: int):
#         self.brand = brand
#         self.year = year
#
#     def info(self):
#         print(f'Brand: {self.brand}, Year: {self.year}')

###############################################################
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

def print_area(shape):
    print(f'Area: {shape.area()}')
circle = Circle(radius=5)
square = Square(side=4)
print_area(circle)
print_area(square)