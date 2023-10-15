# def distance(*args):
#     x1 = args[0]
#     y1 = args[1]
#     x2 = args[2]
#     y2 = args[3]
#     dst = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
#     return dst
# res = distance(int(input()),int(input()),int(input()),int(input()))
# print(res)
#


# 2
# def power(chislo, stepen):
#     res = 1
#     if stepen > 0:
#         for i in range(stepen):
#             res = res * chislo
#     else:
#         for i in range(abs(stepen)):
#             res = res / chislo
#     return res
#
#
# a = float(input())
# n = int(input())
# print(power(a, n))

# # 3
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# print(fib(int(input())))

#
# # 4
# def is_year_leap(year=int(input())):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False
# print(is_year_leap())

# 5
# def square(num = int(input())):
#     return 4 * num,num ** 2,num * (2 ** 0.5)
# print(square())

# 6
# def season(month = int(input())):
#     if month in (12,1,2):return "зима"
#     if month in (3, 4, 5): return "весна"
#     if month in (6, 7, 8): return "лето"
#     if month in (9, 10, 11): return "осень"
# print(season())


#7
# def bank(a,years):
#     if years == 1:
#         return a
#     if years > 1:
#         return bank(a,years - 1) * 0.1 * years + a
# print(bank(int(input()),int(input())))
#


# #8
# def bank(a = int(input()),year = int(input())):
#     for each_year in range(year):
#         a = (a * 1.1)
#     return a
# print(bank())

#9
#
# def bank(a, years):
#     if years == 0:
#         return a
#
#     else:
#         return bank(a + a * 0.1, years - 1)
#
#
# result = bank(1000, 5)
# print(result)
#
#
# # 10
# def is_prime(number=int(input())):
#     Flag = True
#     for i in range(2, number // 2 + 1):
#         if number % i == 0:
#             Flag = False
#         break
#
#     if Flag and number > 1:
#         print("Простое число")
#     else:
#         print("Не подходит")
# print(is_prime())

# 11
# def season(moth):
#
#     if moth == 12 or moth < 3:
#         return 'Зима'
#     elif moth > 2 and moth < 6:
#         return 'Весна'
#     elif moth > 5 and moth < 9:
#         return 'Лето'
#     else:
#         return 'Осень'
#
# year_ = int(input('Введите месяц (Число): '))
#
# if year_ > 0 and year_ <= 12:
#     print(season(year_))
# else:
#     print('Введите значение от 1 до 12!')
#
#
#
# # Правильная дата
#
# def date(d,m,y):
#     if d < 0 or m < 0 or y < 0:
#         return False
#
#     moth = [31,28,31,30,31,30,31,31,30,31,30,31]
#
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         moth[1]=29
#
#     if m >= 1 and m <= 12:
#         if d > 0 and d <= moth[m-1]:
#             return True
#     return False
#
# d_ = int(input('Введите день: '))
# m_ = int(input('Введите месяц: '))
# y_ = int(input('Введите год: '))
#
# print(date(d_, m_, y_))
# тут на несколько задач приведено несколько решений,они сделаны чисто из интереса