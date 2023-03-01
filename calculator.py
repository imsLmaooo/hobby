# Самый простой калькулятор на Python


# Создаем функцию которая принимает
# 2 аргумента a и b потом прибавляем их
# и получаем результат
def add(a, b):
    return a+b # Возвращаем, где эта функция
                       # вызывалась.


# Создаем функцию которая принимает
# 2 аргумента a и b потом отнимаем их
# и получаем результат
def subtract(a, b):
    return a-b # Возвращаем, где эта функция
                      # вызывалась.


# Создаем функцию которая принимает
# 2 аргумента a и b потом умножаем их
# и получаем результат
def multiply(a, b):
    return a*b # Возвращаем, где эта функция
                       # вызывалась.


# Создаем функцию которая принимает
# 2 аргумента a и b потом делим их
# и получаем результат
def divide(a, b):
    return a/b


print_arithmetic_sign = "\
Введите арифметический знак: "


attempts = 3 # Количество попыток
try:
	while attempts > 0: # Цикл для подсчета попыток
		arithmetic_sign = input(print_arithmetic_sign)
		if arithmetic_sign == '+':
		    num = int(input("Введите первое число: "))
		    num_2 = int(input("Введите второе число: "))
		    print(f"{num} + {num_2} =", add(num, num_2))
		    break
		elif arithmetic_sign == '-':
		    num = int(input("Введите первое число: "))
		    num_2 = int(input("Введите второе число: "))
		    print(f"{num} - {num_2} =", subtract(num, num_2))
		    break
		elif arithmetic_sign == '*':
		    num = int(input("Введите первое число: "))
		    num_2 = int(input("Введите второе число: "))
		    print(f"{num} * {num_2} =", multiply(num, num_2))
		    break
		elif arithmetic_sign == '/':
		    num = int(input("Введите первое число: "))
		    num_2 = int(input("Введите второе число: "))
		    print(f"{num} / {num_2} =", divide(num, num_2))
		else:
		    attempts-=1
		    print(f"Некорректный ввод. Осталось {attempts} попыток.")
except ZeroDivisionError: # Деление на ноль
	print(f"Нельзя делить на {num_2}")
except ValueError: # Ошибка значений
	print(f"Принимаются только числа!")