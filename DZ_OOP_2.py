


# class Car:
#     def __init__(self, name='', year=0, volume='', color='', price=''):
#         self.name = name
#         self.year = year
#         self.volume = volume
#         self.color = color
#         self.price = price
#
#     def display_info(self):
#         print(f"Car: {self.name}, Year: {self.year}, Volume: {self.volume}, Color: {self.color}, Price: {self.price}")
#
# my_car1 = Car('Hyundai', 2019, '1.6', 'Бежевый', '1 200 000')
# my_car2 = Car('Renault', 2020, '1.5', 'Красный', ' 1 100 000')
# my_car3 = Car('BMW', 2021, '2.0', 'Черный', '3 000 000')
# my_car4 = Car('Skoda', 2018, '1.4', 'Синий', '800 000')
#
# #  Отобразить информацию об объектах:
# my_car1.display_info()
# my_car2.display_info()
# my_car3.display_info()
# my_car4.display_info()
#
# # Изменить атрибуты:
# my_car1.price = '2 500 000'
# my_car2.price = '1 950 000'
# my_car3.price = '5 500 000'
# my_car4.price = '1 950 050'
#
# my_car5 = Car('Toyota', 2016, '1.8', 'Белая', '2 000 000')
#
# print("\nОбновленная информация о my_car:")
# my_car1.display_info()
# my_car2.display_info()
# my_car3.display_info()
# my_car4.display_info()
# my_car5.display_info()


# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.__balance = initial_balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#
#     def get_balance(self):
#         return self.__balance
#
# def replenish_amount():
#     add_balance = input("Хотите пополнить баланс или отозвать денежные средства? (да/нет): ").strip().lower()
#     if add_balance != 'да':
#         return None
#
#     deposit.amount = int(input("Введите сумму для пополнения: "))
#     account.deposit(depossit.amount)
#
#     withdraw_amount = int(input("Введите сумму для снятия: "))
#     account.withdraw(withdraw_amount)
#
# account = BankAccount(100)
#
# replenish_amount()
# print(account.get_balance())
#
# # Задание 4
# # Создайте класс «Дробь». Необходимо хранить в полях
# # класса: числитель и знаменатель. Реализуйте методы класса
# # для ввода данных, вывода данных, реализуйте доступ к
# # отдельным полям через методы класса. Также создайте
# # методы класса для выполнения арифметических операций
# # (сложение, вычитание, умножение, деление, и т.д.).
#
from __future__ import annotations


class Fraction:
	def __init__(self, numerator: int, denominator: int, int_part: int = 0):
		self.__num: int = numerator + int_part * denominator
		self.__den: int = denominator

	# @property
	# def num(self) -> int:
	# 	return self.__num
	#
	# @num.setter
	# def num(self, value):
	# 	if type(value) == int:
	# 		self.__num = value

	def add(self, fraction: Fraction) -> Fraction:
		num = self.__num * fraction.__den + fraction.__num * self.__den
		den = self.__den * fraction.__den
		return Fraction(num, den)

	def multiply(self, fraction: Fraction) -> Fraction:
		num = self.__num * fraction.__num
		den = self.__den * fraction.__den
		return Fraction(num, den)

	def __str__(self) -> str:
		num = self.__num

		if self.__num > self.__den:
			int_part = int(self.__num / self.__den)
			num -= int_part * self.__den
			return f'{int_part} ({num}/{self.__den})'
		elif self.__num == self.__den:
			return str(int(self.__num / self.__den))

		return f'{self.__num}/{self.__den}'

	def __float__(self):
		return self.__num / self.__den


# f1 = Fraction(2, 3, int_part=3)
f2 = Fraction(3, 3)
#
# f3: Fraction = f1.add(f2)
# f4: Fraction = f3.add(f1)

print(f2)
# print(f.get_num())



