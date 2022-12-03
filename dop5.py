"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных
 индексов.
Пример: - для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


def my_fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return my_fib(n - 2) + my_fib(n - 1)


n = int(input('give me number: '))
our_array = []
for i in range(0, n + 1):
    our_array.insert(0, ((-1) ** (i + 1) * my_fib(i)))
    our_array.append(my_fib(i))
our_array.pop(n)
print(our_array)
