"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    min_arg = min(arg1, arg2, arg3)
    sum_2max_elements = arg1 + arg2 + arg3 - min_arg
    return sum_2max_elements


result = my_func(int(input('give me number1: ')),
                 int(input('give me number2: ')),
                 int(input('give me number3: ')))
print(result)
