# 5 Меньшее из двух
# Пользователь вводит два целых числа. Выведите меньшее из них.

a = int(input('Введите первое число: '))
b = int(input('Введите первое число: '))

print(a if a < b else b)