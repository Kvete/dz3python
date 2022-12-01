"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
 обработку ситуации деления на ноль.
"""


def my_divi(arg1, arg2):
    res = arg1 / arg2
    return round(res, 3)


flag = False
while not flag:
    try:
        num1 = float(input('give me number 1: '))
    except ValueError:
        print("it's not a number")
    else:
        flag = True
while flag:
    try:
        num2 = float(input('give me number 2: '))
    except ValueError:
        print("it's not a number")
    else:
        if num2 == 0:
            print("you can't divide by zero")
        else:
            flag = False
deviation = my_divi(num1, num2)
print(f'{num1}/{num2}={deviation}')
