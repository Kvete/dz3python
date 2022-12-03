"""
 Реализовать функцию, принимающую несколько параметров, описывающих данные
 пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
  Функция должна принимать параметры как именованные аргументы. Реализовать
  вывод данных о пользователе одной строкой.
"""


def man(**kwargs):
    return kwargs


l = man(name=input('give me name: '), surname=input('give me surname: '),
        year=input('give me year: '), city=input('give me city: '),
        email=input('give me email: '), number=input('give me number: '))
result = ''
for i in l:
    result += f'{i}:{l.get(i)}  '
print(result)
