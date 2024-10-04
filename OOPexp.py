



# Домашине до 01.10.2024
# Задание 1
# Создайте класс Device, который содержит информацию об устройстве. Спомощью механизма наследования, реализуйте
# класс CoffeeMachine (содержит информацию о кофемашине), класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке). Каждый из классов должен содержать необходимые для работы методы.

# from __future__ import annotations
#
# import math
# from abc import abstractmethod
#
# class  Device:
#     def __init__(self, manufacturer: str, country: str, price: int):
#         self._manufacturer: str = manufacturer
#         self._country: str = country
#         self.price: int = price
#     @abstractmethod
#     def model(self):
#         return NotImplementedError('Метод должен быыть опредеелеен')
#
#     @abstractmethod
#     def about(self):
#         return NotImplementedError('Метод должен быыть опредеелеен')
#
#     @abstractmethod
#     def socet(self):
#         return NotImplementedError('Метод должен быыть опредеелеен')
#
# class CoffeeMachine(Device):
#     def __init__(self, manufacturer: str, country: str, price: int, power_volts: str, frame: str):
#         super().__init__(manufacturer, country, price)
#         self._power_volts: str = power_volts
#         self._frame: str = frame
#     def model(self):
#         print(f'Модель: {self._manufacturer}')
#
#     def about(self):
#         print(f' Произведено в {self._country} - (Имеет оптовую цену): {self.price} $ - питание расчитано на ({self._power_volts}), металлический корпус, {self._frame},')
#
#     def socet(self):
#         print(f'Розетка евро')


#     def guarantee(self):
#         print('1 год')
#
# class Blender(Device):
#     def __init__(self, manufacturer: str, country: str, price: int, power_volts: str, frame: str):
#         super().__init__(manufacturer, country, price)
#         self._power_volts: str = power_volts
#         self._frame: str = frame
#
#     def model(self):
#         print(f'Модель: {self._manufacturer}')
#
#     def about(self):
#         print(f' Произведено в {self._country} - (Имеет оптовую цену): {self.price} - питание расчитано на ({self._power_volts}), пластиковый корпус, {self._frame},')
#
#     def socet(self):
#         print(f'Розетка евро')
#
#     def guarantee(self):
#         print('1,5 год')
#
#
# class MeatGrinder(Device):
#     def __init__(self, manufacturer: str, country: str, price: int, power_volts: str, frame: str):
#         super().__init__(manufacturer, country, price)
#         self._power_volts: str = power_volts
#         self._frame: str = frame
#
#     def model(self):
#         print(f'Модель: {self._manufacturer}')
#
#     def about(self):
#         print(f' Произведено в {self._country} - (Имеет оптовую цену): {self.price} - питание расчитано на ({self._power_volts}), металлический корпус, {self._frame},')
#
#     def socet(self):
#         print(f'Розетка евро')


    # def guarantee(self):
    #     print('2 года')

#

# Задание 2
# Создайте класс Ship, который содержит информацию о корабле.
# С помощью механизма наследования, реализуйте класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.



# from __future__ import annotations
#
# import math
# from abc import abstractmethod
#
# class  Ship:
#     def __init__(self, name: str, weight: str, price: int):
#         self._name: str = name
#         self._weight: str = weight
#         self.price: int = price
#     @abstractmethod
#     def displacement(self):
#         return NotImplementedError('Метод должен быыть опредеелеен')
#
#     @abstractmethod
#     def about(self):
#         return NotImplementedError('Метод должен быыть опредеелеен')
#
#     @abstractmethod
#     def armament(self):
#         return NotImplementedError('Метод должен быыть опредеелеен')
#
# class Frigate(Ship):
#     def __init__(self, name: str, weight: str, price: int, produced: str, country: str):
#         super().__init__(name, weight, price)
#         self._produced: str = produced
#         self._country: str = country
#     def displacement(self):
#         print(f'Водоизмещение 25 тонн')
#
#     def about(self):
#         print(f' Произведено в {self._produced}  - стоимость производства: {self.price} $ - масса корбля ({self._weight})')
#
#     def armament(self):
#         print(f'на вооружение 25 ракет, 4 торпеды')
#
#     def affiliation(self):
#         print(f'находится на вооружении {self._country}')
#
#
# class Destroyer(Ship):
#     def __init__(self, name: str, weight: str, price: int, produced: str, country: str):
#         super().__init__(name, weight, price)
#         self._produced: str = produced
#         self._country: str = country
#     def displacement(self):
#         print(f'Водоизмещение 23 тонн')
#
#     def about(self):
#         print(f' Произведено в {self._produced}  - стоимость производства: {self.price} $ - масса корбля ({self._weight})')
#
#     def armament(self):
#         print(f'на вооружение 50 ракет, 4 торпеды')
#
#     def affiliation(self):
#         print(f'находится на вооружении {self._country}')
#
# class Cruiser(Ship):
#     def __init__(self, name: str, weight: str, price: int, produced: str, country: str):
#         super().__init__(name, weight, price)
#         self._produced: str = produced
#         self._country: str = country
#     def displacement(self):
#         print(f'Водоизмещение 30')
#
#     def about(self):
#         print(f' Произведено в {self._produced}  - стоимость производства: {self.price} $ - масса корбля ({self._weight})')
#
#     def armament(self):
#         print(f'на вооружение 43 ракет, 4 торпеды')
#
#     def affiliation(self):
#         print(f'находится на вооружении {self._country}')
#


# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.


# class Money:
#     def __init__(self, dollar: float, euro: float, hryvnia: float, cents: float, eurocents: float, kopecks: float):
#         self._dollar: float = dollar
#         self._euro: float = euro
#         self._hryvnia: float = hryvnia
#         self._cents: float = cents
#         self._eurocents: float = eurocents
#         self._kopecks: float = kopecks
#
#     def convector_to_usd(self):
#         euro_to_usd = 1.12
#         hryvnia_to_usd = 0.027
#         cents_to_usd = 0.01
#         eurocents_to_usd = 0.011
#         kopecks_to_usd = 0.00027
#
#         total_usd = (self._dollar + self._euro * euro_to_usd + self._hryvnia * hryvnia_to_usd + self._cents * cents_to_usd + self._eurocents * eurocents_to_usd + self._kopecks * kopecks_to_usd)
#
#         return total_usd
#
#     def summa(self):
#         print(f'Сумма в долларах: {self._dollar} USD, сумма в центах: {self._cents} cents')
#         print(f'Сумма в евро: {self._euro} EUR, сумма в евроцентах: {self._eurocents} eurocents')
#         print(f'Сумма в гривнах: {self._hryvnia} UAH, сумма в копейках: {self._kopecks} kopecks')
#         total_usd = self.convector_to_usd()
#         print(f'Общая сумма в долларах: {total_usd:.2f} USD')
#
#
# money = Money(dollar = 100, euro= 200, hryvnia= 300, cents= 50, eurocents= 75, kopecks= 150)
# money.summa()




# Домашние до 03.10.2024
# Задание 1
# Создать базовый класс Фигура с методом для подсчета площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими методами для подсчета площади.


# from __future__ import  annotations
#
# import  math
# from  abc import  abstractmethod
#
# class Coordinated:
#     def __init__(self, x: float, y: float):
#         self._x: float = x
#         self._y: float = y
#
#     def distance(self, other: Coordinated) -> float:
#         return  math.hypot(math.fabs(self._x - other._x), math.fabs(self._y - other._y))
#
# class Figure:
#     @abstractmethod
#     def area(self) -> float:
#         raise NotImplementedError('Необходимо реализовать метод area класса Figure')
#
#     @abstractmethod
#     def perimeter(self) -> float:
#         raise NotImplementedError('Необходимо реализовать метод area класса Figure')
#
# class Circle(Coordinated, Figure):
#     def __init__(self, x: float, y: float, radius: float):
#         super().__init__(x, y)
#         self._radius: float = radius
#
#     def area(self) -> float:
#         return math.pi * self._radius ** 2
#
#     def perimeter(self) -> float:
#         return 2 * math.pi * self._radius
#
#     def about(self):
#         s_circle = self.area()
#         p_circle = self.perimeter()
#         print(f' Площадь круга равна {s_circle}), периметр круга равен {p_circle}')
#
# class Square(Figure):
#     def __init__(self, side: float):
#         self._side: float = side
#
#     def area(self) -> float:
#         return self._side ** 2
#
#     def perimeter(self) -> float:
#         return self._side * 4
#
#     def about(self):
#         s_square = self.area()
#         p_square = self.perimeter()
#         print(f' Площадь квадрата равна {s_square}), периметр квадрата равен {p_square}')
#
#
# class Tirangle(Figure):
#     def __init__(self, base: float, height: float):
#         self._base: float = base
#         self._height: float = height
#
#     def area(self) -> float:
#         return (self._base * self._height) / 2
#
#     def perimeter(self) -> float:
#         return self._base * 3
#
#     def about(self):
#         s_tirangle = self.area()
#         p_tirangle = self.perimeter()
#         print(f' Площадь квадрата равна {s_tirangle}), периметр квадрата равен {p_tirangle}')
#

# Задание 2
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
# информацию о фигуре).

# from __future__ import  annotations
#
# import  math
# from  abc import  abstractmethod
#
# class Coordinated:
#     def __init__(self, x: float, y: float):
#         self._x: float = x
#         self._y: float = y
#
#     def distance(self, other: Coordinated) -> float:
#         return  math.hypot(math.fabs(self._x - other._x), math.fabs(self._y - other._y))
#
# class Figure:
#     @abstractmethod
#     def area(self) -> float:
#         raise NotImplementedError('Необходимо реализовать метод area класса Figure')
#
#     @abstractmethod
#     def perimeter(self) -> float:
#         raise NotImplementedError('Необходимо реализовать метод area класса Figure')
#
#     def __int__(self) -> int:
#         return int(self.area())
#
#     def __str__(self) -> str:
#         return f"{self.__class__.__name__}: Площадь = {self.area()}, Периметр = {self.perimeter()}"
#
# class Circle(Coordinated, Figure):
#     def __init__(self, x: float, y: float, radius: float):
#         super().__init__(x, y)
#         self._radius: float = radius
#
#     def area(self) -> float:
#         return math.pi * self._radius ** 2
#
#     def perimeter(self) -> float:
#         return 2 * math.pi * self._radius
#
#     def about(self):
#         s_circle = self.area()
#         p_circle = self.perimeter()
#         print(f' Площадь круга равна {s_circle}), периметр круга равен {p_circle}')
#
# class Square(Figure):
#     def __init__(self, side: float):
#         self._side: float = side
#
#     def area(self) -> float:
#         return self._side ** 2
#
#     def perimeter(self) -> float:
#         return self._side * 4
#
#     def about(self):
#         s_square = self.area()
#         p_square = self.perimeter()
#         print(f' Площадь квадрата равна {s_square}), периметр квадрата равен {p_square}')
#
#
# class Tirangle(Figure):
#     def __init__(self, base: float, height: float):
#         self._base: float = base
#         self._height: float = height
#
#     def area(self) -> float:
#         return (self._base * self._height) / 2
#
#     def perimeter(self) -> float:
#         return self._base * 3
#
#     def about(self):
#         s_tirangle = self.area()
#         p_tirangle = self.perimeter()
#         print(f' Площадь квадрата равна {s_tirangle}), периметр квадрата равен {p_tirangle}')
#
# circle = Circle(0, 0, 5)
# print(circle)
# print(int(circle))
#
# square = Square(4)
# print(square)
# print(int(square))
#
# triangle = Tirangle(3,4)
# print(triangle)
# print(int(triangle))



# Задание 3
# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
#
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами
# этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о
# каждой из фигур.


# from __future__ import  annotations
# import  math
# from  abc import ABC, abstractmethod
# class Shape:
#     def __init__(self, x: float, y: float):
#         self._x: float = x
#         self._y: float = y
#
#     def distance(self, other: 'Shape') -> float:
#         return  math.hypot(math.fabs(self._x - other._x), math.fabs(self._y - other._y))
#
# class Figure(ABC):
#
#     @abstractmethod
#     def show(self):
#         raise NotImplementedError('Необходимо реализовать метод show класса Figure')
#
#     @abstractmethod
#     def save(self):
#         raise NotImplementedError('Необходимо реализовать метод save класса Figure')
#
#     @abstractmethod
#     def load(self):
#         raise NotImplementedError('Необходимо реализовать метод load класса Figure')
#
#
#
# class Square(Shape, Figure):
#     def __init__(self, x: float, y: float, side: float):
#         super().__init__(x, y)
#         self._side: float = side
#
#     def area(self) -> float:
#         return self._side ** 2
#
#     def __str__(self):
#         return f"Квадрат: {super().__str__()}, сторона: {self._side}"
#
#     def show(self):
#         return f' Координаты левого верхнего угла квадрата: ({self._x},{self._y}), сторона квадрата: {self._side}'
#
#
#     def save(self, filename: str):
#         with open(filename, 'a') as file:
#             file.write(f'Square: x={self._x}, y={self._y}, side={self._side}\n')
#         return f'Data saved to {filename}'
#
#     def load(self, filename: str):
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 if line.startswith('Square'):
#                     parts = line.split(',')
#                     x = float(parts[0].split('=')[1].strip())
#                     y = float(parts[1].split('=')[1].strip())
#                     side = float(parts[2].split('=')[1].strip())
#                     self._x = x
#                     self._y = y
#                     self._side = side
#                     return f'Loaded Square: x={self._x}, y={self._y}, side={self._side}'
#             return 'No Square data found in the file'
#
#
#
# class Rectangle(Shape, Figure):
#     def __init__(self, x: float, y: float, width: float, height: float):
#         super().__init__(x, y)
#         self._width: float = width
#         self._height: float = height
#
#     def area(self) -> float:
#         return self._width * self._height
#
#     def __str__(self):
#         return f"Прямоугольник: {super().__str__()}, ширина: {self._width}, высота: {self._height}"
#
#     def show(self):
#         return f' Координаты левого верхнего угла прямоугольника: {self._x},{self._y}), ширина: {self._width}, высота: {self._height}'
#
#
#     def save(self, filename: str):
#         with open(filename, 'a') as file:
#             file.write(f'Rectangle: x={self._x}, y={self._y}, width={self._width}, height={self._height}\n')
#         return f'Data saved to {filename}'
#
#     def load(self, filename: str):
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 if line.startswith('Rectangle'):
#                     parts = line.split(',')
#                     x = float(parts[0].split('=')[1].strip())
#                     y = float(parts[1].split('=')[1].strip())
#                     width = float(parts[2].split('=')[1].strip())
#                     height = float(parts[3].split('=')[1].strip())
#                     self._x = x
#                     self._y = y
#                     self._width = width
#                     self._height = height
#                     return f'Loaded Rectangle: x={self._x}, y={self._y}, width={self._width}, height={self._height}'
#             return 'No Square data found in the file'
#
#
# class Circle(Shape, Figure):
#     def __init__(self, x: float, y: float, radius: float):
#         super().__init__(x, y)
#         self._radius: float = radius
#
#     def area(self) -> float:
#         return 3.14159 * self._radius ** 2
#
#     def __str__(self):
#         return f"Круг: {super().__str__()}, радиус: {self._radius}"
#
#     def show(self):
#         return f' Координаты центра окружности: {self._x},{self._y}), радиус окружности: {self._radius}'
#
#     def save(self, filename: str):
#         with open(filename, 'a') as file:
#             file.write(f'Circle: x={self._x}, y={self._y}, radius={self._radius}\n')
#         return f'Data saved to {filename}'
#
#     def load(self, filename: str):
#         with (open(filename, 'r') as file):
#             lines = file.readlines()
#             for line in lines:
#                 if line.startswith('Circle'):
#                     parts = line.split(',')
#                     x = float(parts[0].split('=')[1].strip())
#                     y = float(parts[1].split('=')[1].strip())
#                     radius = float(parts[2].split('=')[1].strip())
#                     self._x = x
#                     self._y = y
#                     self._radius = radius
#                     return f'Loaded Square: x={self._x}, y={self._y}, radius={self._radius}'
#             return 'No Square data found in the file'
#
#
#
# class Ellipse(Shape, Figure):
#     def __init__(self, x: float, y: float, width: float, height: float):
#         super().__init__(x, y)
#         self._width = width
#         self._height = height
#
#     def area(self) -> float:
#         return 3.14159 * (self._width / 2) * (self._height / 2)
#
#     def show(self):
#         return f' Координаты левого верхнего угла прямоугольника: {self._x},{self._y}), ширина: {self._width}, высота: {self._height}'
#
#     def __str__(self):
#         return f"Эллипс: {super().__str__()}, ширина: {self._width}, высота: {self._height}"
#
#     def save(self, filename: str):
#         with open(filename, 'a') as file:
#             file.write(f'Ellipse: x={self._x}, y={self._y}, width={self._width}, height={self._height}\n')
#
#     def load(self, filename: str):
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 if line.startswith('Ellipse'):
#                     parts = line.split(',')
#                     self._x = float(parts[0].split('=')[1].strip())
#                     self._y = float(parts[1].split('=')[1].strip())
#                     self._width = float(parts[2].split('=')[1].strip())
#                     self._height = float(parts[3].split('=')[1].strip())
#                     return f'Loaded Ellipse: x={self._x}, y={self._y}, width={self._width}, height={self._height}'
#             return 'No Ellipse data found in the file'
#
#
# filename = "shapes.txt"  # Задайте имя файла
#
# square = Square(2, 3, 5)
# print(str(square))
# print(square.show())  # Убедитесь, что метод show вызывается для отображения информации
# print(square.save(filename))
#
# rectangle = Rectangle(2, 3, 4, 6)
# print(str(rectangle))
# print(rectangle.show())
# print(rectangle.save(filename))
#
# circle = Circle(2, 3, 5)
# print(str(circle))
# print(circle.show())
# print(circle.save(filename))
#
# ellipse = Ellipse(2, 3, 10, 15)
# print(str(ellipse))
# print(ellipse.show())
# print(ellipse.save(filename))
#
# print("\nЗагрузка данных:")
# new_square = Square(0, 0, 0)
# print(new_square.load(filename))
#
# new_rectangle = Rectangle(0, 0, 0, 0)
# print(new_rectangle.load(filename))
#
# new_circle = Circle(0, 0, 0)
# print(new_circle.load(filename))
#
# new_ellipse = Ellipse(0, 0, 0, 0)
# print(new_ellipse.load(filename))
#
#






