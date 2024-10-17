
# OOP-7
# Задача 5: Магические методы
#
# Описание: Создайте класс ComplexNumber, который будет представлять
# комплексное число и реализуйте сложение и вычитание комплексных чисел,
# используя магические методы add() и sub().
#
# Условия:
#
#  • Конструктор должен принимать действительную и мнимую части.
#  • Реализуйте магические методы для сложения и вычитания.
#
# class ComplexNumber:
#     i: complex = 1j
#     def __init__(self, a: int, b: int, c: int, d: int):
#         self._a: int = a
#         self._b: int = b
#         self._c: int = c
#         self._d: int = d
#
#     def __add__(self, other):
#         real_part = self._a + other._c
#         imaginary_part = self._b + other._d
#         return ComplexNumber(real_part, imaginary_part, 0, 0)
#
#     def __sub__(self, other):
#         real_part = self._a - other._c
#         imaginary_part = self._b - other._d
#         return ComplexNumber(real_part, imaginary_part, 0, 0)
#
# cn1 = ComplexNumber(4, 3, 5,7)
# cn2 = ComplexNumber(2, 8, 9, 4)
#
# result_add = cn1 + cn2
# result_sub = cn1 - cn2
#
# print(f'Результат сложения: ({result_add._a}, {result_add._b})')
# print(f'Результат выситания: ({result_sub._a}, {result_sub._b})')
#
#

# Задача 6: Инкапсуляция
#
# Описание: Создайте класс Car, который содержит информацию о марке
# автомобиля, максимальной скорости и текущей скорости. Инкапсулируйте
# переменные с текущей скоростью, чтобы нельзя было напрямую её изменять.
#
# Условия:
#
#  • Создайте конструктор, принимающий марку и максимальную скорость.
#  • Создайте методы для увеличения и уменьшения скорости, контролируя,
# чтобы скорость не превышала максимальную.
#  • Добавьте метод для отображения текущей скорости.

# import time
#
# class Car:
#     def __init__(self, model: str, max_speed: int, current_speed: int):
#         self.__model: str = model
#         self.__max_speed: int = max_speed
#         self.__current_speed: int = current_speed
#
#     def increase_speed(self):
#         while self.__current_speed < self.__max_speed:
#             self.__current_speed += 1
#             print(f'Увеличение скорости... Текущая скорость - {self.__current_speed}')
#             time.sleep(1)
#
#     def decrease_in_speed(self):
#         while self.__current_speed > 0:
#             self.__current_speed -= 1
#             print(f'Уменьшение скорости... Текущая скорость - {self.__current_speed}')
#             time.sleep(1)
#
#     def get_current_speed(self):
#         return self.__current_speed
#
#     def __str__(self):
#         return f'Текущая скорость - {self.__current_speed}'
#
#
# my_car = Car("Toyota", 10, 0)
#
# print(my_car)
#
# my_car.increase_speed()
#
# print(my_car)
#
# my_car.decrease_in_speed()
#
# print(my_car)
#



#  • Класс Square должен принимать длину стороны, а класс Triangle —
# основание и высоту.
#  • Метод get_area() должен возвращать площадь фигуры.
#
# Каждая из этих задач поможет вам лучше понять принципы ООП, такие как
# инкапсуляция, наследование, полиморфизм и абстракция.


# from __future__ import annotations
# import math
# from abc import abstractmethod, ABC
#
# class Figure:
#     @staticmethod
#     @abstractmethod
#     def get_area(self) -> float:
#         raise NotImplementedError('Необходимо определить метод')
#
#     def __str__(self) -> str:
#         raise NotImplementedError('Необходимо определить метод')
#
#
# class Square(Figure):
#     def __init__(self, side: float):
#         self.__side: float = side
#
#     def get_area(self) -> float:
#         return self.__side ** 2
#
#     def __str__(self) -> float:
#         return f'Квадрат стороной {self.__side} имеет площадь {self.get_area()}'
#
#
# class Triangle(Figure):
#     def __init__(self, height: float, base: float):
#         self.__height: float = height
#         self.__base: float = base
#
#     def get_area(self) -> float:
#         return (self.__base * self.__height) / 2
#
#     def __str__(self) -> float:
#         return f'Треугольник с основанием {self.__base} высотой {self.__height} имеет площадь {self.get_area()}'
#
#
# square = Square(4)
# print(square)
#
# triangle = Triangle(3, 5)
# print(triangle)
#


