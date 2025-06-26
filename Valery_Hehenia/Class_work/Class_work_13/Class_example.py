#КЛАСС о объект
class Car:
    #Констркуктор (инициализатор)
    def __init__(self, brand: str, color: str):
        #Атрибуты объектов
        self.brand = brand
        self.color = color
    #Методы объектов
    def driver(self):
        print(f'{self.brand} {self.color} is driving.')

#Создание объектов
ford = Car('Ford', 'red')
tesla = Car('Tesla', 'blue')

ford.driver()
tesla.driver()

#################################################################################
#Наследование
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speek(self):
        print('Звук животного')


class Dog(Animal):

    def speek(self):
        print('Гав')


class Cat(Animal):

    def speek(self):
        print('Мяу')

dog = Dog('bobik')
cat = Cat('murzik')

dog.speek()
cat.speek()

###############################################################

#Инкапсуляция
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0


    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
    def get_balance(self)-> float:
        return self.__balance


name_account = BankAccount('Valery')
name_account.deposit(1000)
print(name_account.get_balance())


###############################################################

#Полиморфизм
def animal_sound(animals: list[Animal]):
    for animal in animals:
        animal.speek()

zoo = [Dog('bobik'), Cat('murzik')]
animal_sound(zoo)


###############################################################