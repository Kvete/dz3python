"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def binary(number):
    list_binary = []
    while number > 0:
        list_binary.append(str(number % 2))
        number //= 2
    list_binary.reverse()
    return list_binary


n = int(input("give me number: "))
print(f'my  function:{n} -> {"".join(binary(n))}')
print(f'bin function:{n}->{bin(n)}')
