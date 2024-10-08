
# Задание 1
# Создайте функцию, возвращающую список со всеми простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько секунд, потребовалось для
# вычисления всех простых чисел. Отобразите на экран количество секунд и простые числа.


# import time
# def time_worker(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time() - start
#         print(f'Функция {func.__name__} выполнялась {end} с.')
#         return result
#     return wrapper
#
# @time_worker
# def number_list(my_list):
#     for i in my_list:
#         print(i)

# number_list(range(1, 1000))


# Задание 2
# Добавьте к первому заданию возможность передавать границы диапазона для поиска всех
# простых чисел.


# import time
# def time_worker(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time() - start
#         print(f'Функция {func.__name__} выполнялась {end} с.')
#         return result
#     return wrapper
#
# @time_worker
# def number_list(my_list):
#     for i in my_list:
#         is_prime = True
#         if i < 2:
#             continue
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(i)
#
# number_list(range(1, 1000))


# Задание 3
# Каждый год ваша компания предоставляет различным государственным организациям финансовую
# отчетность. В зависимости от организации форматы отчетности разные. Используя механизм
# декораторов, решите вопрос отчетности для организаций.


# from __future__ import  annotations
# import math
# from  abc import abstractmethod
# class CompanyImportChina:
#     def __init__(self, name: str, profit: float, costs: float, tax: float):
#         self._name: str = name
#         self._profit: float = profit
#         self._costs: float = costs
#         self._tax: float = tax
#
#     @staticmethod
#     def regional_tax_dec(func):
#         def wrapper(self):
#             costs = func(self)
#             region = (self._profit - self._costs) * 0.17
#             return costs, region
#         return wrapper
#
#     @abstractmethod
#     def federal_tax_dec(func):
#         def wrapper(self):
#             costs = func(self)
#             federal = (self._profit - self._costs) * 0.03
#             return federal
#         return wrapper
#
# class HoldingSales(CompanyImportChina):
#     def __init__(self,  name: str, profit: float, costs: float, tax: float, profit_holding: float):
#         super().__init__(name, profit, costs, tax)
#         self._profit_holding: float = profit_holding
#
#     @CompanyImportChina.regional_tax_dec
#     def costs_holding_sum_reg(self):
#         general_profit = self._profit + self._profit_holding
#         return general_profit
#
#     @CompanyImportChina.federal_tax_dec
#     def costs_holding_sum_fed(self):
#         general_profit = self._profit + self._profit_holding
#         return general_profit
#
#     def __str__(self) -> str:
#         region_tax = (self._profit - self._costs) * 0.17
#         federal_tax = (self._profit - self._costs) * 0.03
#         return (f'Холдинг: {self._name}\n'
#                 f'Прибыль компании: {self._profit}\n'
#                 f'Прибыль холдинга: {self._profit_holding}\n'
#                 f'Затраты на на осуществление деятельности: {self._costs}\n'
#                 f'Региональный налоговый сбор: {region_tax}\n'
#                 f'Федеральный налоговый сбор: {federal_tax}\n')
#
#
# holding = HoldingSales(name='Торговый', profit=100000, costs=30000, tax=0, profit_holding=20000)
#
# costs, region = holding.costs_holding_sum_reg()
# federal = holding.costs_holding_sum_fed()
#
# print(holding)
# print(f'Региональный налог: {region}')
# print(f'Федеральный налог: {federal}')
#
#
#
#
# class HoldingExport(CompanyImportChina):
#     def __init__(self,  name: str, profit: float, costs: float, tax: float, profit_holding: float):
#         super().__init__(name, profit, costs, tax)
#         self._profit_holding: float = profit_holding
#
#     @CompanyImportChina.regional_tax_dec
#     def costs_holding_sum_reg(self):
#         general_profit = self._profit + self._profit_holding
#         return general_profit
#
#     @CompanyImportChina.federal_tax_dec
#     def costs_holding_sum_fed(self):
#         general_profit = self._profit + self._profit_holding
#         return general_profit
#
#     def __str__(self) -> str:
#         region_tax = (self._profit - self._costs) * 0.17
#         federal_tax = (self._profit - self._costs) * 0.03
#         return (f'Холдинг: {self._name}\n'
#                 f'Прибыль компании: {self._profit}\n'
#                 f'Прибыль холдинга: {self._profit_holding}\n'
#                 f'Затраты на на осуществление деятельности: {self._costs}\n'
#                 f'Региональный налоговый сбор: {region_tax}\n'
#                 f'Федеральный налоговый сбор: {federal_tax}\n')
#
#
# holding = HoldingExport(name='Экспорта', profit=200000, costs=40000, tax=0, profit_holding=30000)
#
# costs, region = holding.costs_holding_sum_reg()
# federal = holding.costs_holding_sum_fed()
#
# print(holding)
# print(f'Региональный налог: {region}')
# print(f'Федеральный налог: {federal}')
# print()
#
#

# Другой способ, раширенные условия. НЕ ЗАКОНЧЕН


# from __future__ import  annotations
# import math
# from  abc import abstractmethod
# class CompanyImportChina:
#     def __init__(self, name: str, enterprise: str, quarter: str, profit: int, attachments: int, insurance: int, salaries: int, costs: int, tax: int, profit_holding: int):
#         self._name: str = name
#         self._enterprise: str = enterprise
#         self._quarter: str = quarter
#         self._profit: int = profit
#         self._attachments: int = attachments
#         self._insurance: int = insurance
#         self._salaries: int = salaries
#         self._costs: int = costs
#         self._tax = tax
#         self._profit_holding = profit_holding
#
#
#     @abstractmethod
#     def costs_holding(self):
#         pass
#
#     @staticmethod
#     def regional_tax_dec(func):
#         def wrapper(self):
#             result = func(self)
#             region = ((self._profit + self._profit_holding) - self._costs) * 17 / 100
#             return result, region
#         return wrapper
#
#     @staticmethod
#     def federal_tax_dec(func):
#         def wrapper(self):
#             results, region = func(self)
#             federal = ((self._profit + self._profit_holding) - self._costs) * 3 / 100
#             return results, region, federal
#         return wrapper
#
#
# class HoldingSales(CompanyImportChina):
#     def __init__(self, name: str, enterprise: str, quarter: str, profit: int, attachments: int, insurance: int, salaries: int, costs: int, tax: int, profit_holding: int):
#         super().__init__(name, enterprise, quarter, profit, attachments, insurance, salaries, costs, tax)
#         self._profit_holding = profit_holding
#
#
#     def costs_holding(self):
#         costs = (self._attachments + self._insurance + self._salaries)
#         return costs
#
#     @CompanyImportChina.regional_tax_dec
#     @CompanyImportChina.federal_tax_dec
#     def tax_holding(self):
#         return self.costs_holding()
#
#     def __str__(self) -> str:
#         return (f'Холдинг: {self._name}\n'
#                 f'Вид деятельности: {self._enterprise}\n'
#                 f'Квартал: {self._quarter}\n'
#                 f'Чистая прибыль: {self._profit}\n'
#                 f'Затраты на осуществление деятельности: {self._attachments}\n'
#                 f'Расходы на страховые отчисления: {self._insurance}\n'
#                 f'Затраты на выплаты заработных плат: {self._salaries}\n'
#                 f'Общие расходы: {self._costs}\n'
#                 f'Прибыль внутри холдинга: {self._profit_holding}\n')
#
#
#     @staticmethod
#     def create_report():
#         add_name = input('Сформировать отчет за квартал? (да/нет):').strip().lower()
#         if add_name != 'да':
#             return None
#
#         name = input('Введите название холдинга: ').strip().lower()
#         enterprise = input('Укажите вид деятельности холдинга: ').strip().lower()
#         quarter = input('Укажите отчетный квартал (в формате: I, II, III, IV): ')
#         profit = int(input('Укажите прибыль холдинга за квартал: '))
#         attachments = int(input(
#             'Укажите сумму всех коммерческих затрах, включая вложенные в оборот, аренду, коммунальные, транспортные и офиссные расходы: '))
#         insurance = int(input('Укажите сумму страховых отчислений, включая взносы в ПФР и страхование предпринимательских рисков: '))
#         salaries = int(input('Укажите суммы расходов на заработные платы: '))
#         profit_holding = int(input('Укажите сумму прибыли холдинга: '))
#         return HoldingSales(name=name, enterprise=enterprise, quarter=quarter, profit=profit,
#                             attachments=attachments, insurance=insurance, salaries=salaries,
#                             costs=attachments + insurance + salaries, tax=0, profit_holding=profit_holding)
#
# def main():
#     holdings = []
#     while True:
#         hold = create_report()
#         if hold is None:
#             break
#         holdings.append(hold)
#
#     for holding in holdings:
#         results = holding.tax_holding()  # Здесь уже сработают декораторы
#         print(f'Результаты для {holding._name}:')
#         print(f'Общие затраты: {results[0]}')
#         print(f'Региональный налог: {results[1]}')
#         print(f'Федеральный налог: {results[2]}')
#         print()  # Для разделения вывода
#
# if __name__ == "__name__":
#     main()
#






