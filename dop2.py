"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""


def my_func(input_array):
    new_array = []
    for i in range((len(input_array) + 1) // 2):
        new_array.append(
            input_array[i] * input_array[len(input_array) - i - 1])
    return new_array


user_array = [2, 3, 4, 5, 6]
print(f'{user_array}=>{my_func(user_array)}')
