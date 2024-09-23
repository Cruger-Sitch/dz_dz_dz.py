


# Задание 2
# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температурыи возвращать это значение с помощью статического метода.

# class TemperatureTranslation:
#     def __init__(self, celsius: float = None, fahrenheit: float = None):
#         self.__celsius: float = celsius
#         self.__fahrenheit: float = fahrenheit
#
#     @staticmethod
#     def froom_celsius_to_fahrenheit(celsius: float) -> float:
#         return (celsius * 9/5) + 32
#
#     @staticmethod
#     def froom_fahrenheit_to_celsius(fahrenheit: float) -> float:
#         return (fahrenheit - 32) * 5/9
#
# celsius_temp = 500
# fahrenheit_temp = 110
#
# a = TemperatureTranslation.froom_celsius_to_fahrenheit(celsius_temp)
# b = TemperatureTranslation.froom_fahrenheit_to_celsius(fahrenheit_temp)
#
#
# print(f'Температура в переводе с цельсия в фаренгейт составит: {a}')
# print(f'Температура в переводе с фаренгейт в цельсия составит: {b}')
#



# Задание 3
# Создайте класс для перевода из метрической системы в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно реализуйте перевод мер длины.

class Length_distance:
    @staticmethod
    def kilometer_mile(kilometer: float) -> float:
        return kilometer / 0.62

    @staticmethod
    def meter_yard(meter: float) -> float:
        return  meter * 1.09

    @staticmethod
    def centimeter_inch(centimeter: float) -> float:
        return centimeter / 0.39

    @staticmethod
    def millimeter_inch(millimeter: float) -> float:
        return millimeter / 0.039


kilometer_km = 2
meter_m = 2
centimeter_cm = 2
millimeter_mm = 2

a = Length_distance.kilometer_mile(kilometer_km)
b = Length_distance.meter_yard(meter_m)
c = Length_distance.centimeter_inch(centimeter_cm)
d = Length_distance.millimeter_inch(millimeter_mm)

print(f'Расстояниее в {kilometer_km} км соответствует {a} милям')
print(f'Длинна в {meter_m} м соответствует {b} ярд')
print(f'Длина в {centimeter_cm} см соответствует {c} дюйм')
print(f' Длина {millimeter_mm} мл соответствует {d} дюйм')

#

# Рассмотрим объект «Программист», который задаётся именем, должностью и количеством
# отработанных часов. Каждая должность имеет собственный оклад (заработную плату за
# час работы). В нашей импровизированной компании существуют 3 должности:
# Junior — с окладом 10 тугриков в час;
# Middle — с окладом 15 тугриков в час;
# Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое
# повышение. Напишите класс Programmer, который инициализируется именем и должностью
# (отработка у нового работника равна нулю). Класс реализует следующие методы:
# work(time) — отмечает новую отработку в количестве часов time;
# rise() — повышает программиста;
# info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных
# часов>ч. <накопленная зарплата> тгр.
#


# from __future__ import annotations
#
#
# class Programmer:
#     def __init__(self, name='', time=0, level='', salary=0, rise=''):
#         self.__name = name
#         self.__time = time
#         self.__level = level.lower()
#         self.__salary = salary
#         self.__rise = rise
#
#     @property
#     def work(self):
#         if self.__level == 'junior':
#             self.__salary = self.__time * 10
#         elif self.__level == 'middle':
#             self.__salary = self.__time * 15
#         elif self.__level == 'senior':
#             self.__salary = self.__time * 20
#         else:
#             raise  ValueError('Не правильно введен уровень, введите (Junior, Middle, Senior)')
#         return  self.__salary
#
#     def apply_rise(self):
#         if self.__rise == 'да':
#             self.__salary += self.__time * 1
#         return  self.__salary
#
#
# def create_programmer():
#     add_name = input("Добавить нового работника? (да/нет): ").strip().lower()
#     if add_name != 'да':
#         return None
#
#     name = input('Введите ФИО работника: ').strip().lower()
#     level = input('Введите уровень работника (Junior, Middle, Senior): ').strip().lower()
#     time = int(input('Введите количество отработанных часов: '))
#     rise = input('Повысить программиста? (да/нет)').strip().lower()
#     return Programmer(name=name, time=time, level=level, rise=rise)
#
# programmers = []
# while True:
#     prog = create_programmer()
#     if prog is None:
#         break
#     programmers.append(prog)
#
# for programmer in programmers:
#     salary = programmer.work
#     final_salary = programmer.apply_rise()
#     print(f'зарбплата программиста {programmer._Programmer__name}: {final_salary}')




