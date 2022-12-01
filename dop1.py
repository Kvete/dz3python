"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""


def my_func(input_array):
    summ = 0
    for i in range(1, len(input_array), 2):
        summ += input_array[i]
    return summ


user_array = [2, 3, 5, 9, 3]
print(my_func(user_array))
