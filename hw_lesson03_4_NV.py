# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# ** Подсказка:** попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    return 1 / (x ** abs(y))


print(f"Результат решения №1, {my_func(2, -3)}")


def my_func(x, y):
       res = 1
       for i in range(abs(y)):
           res *= x
       if y >= 0:
          return res
       else:
          return 1/res

print(my_func(float(input("Введите число для возведения в степень")),int(input("Введите степень"))))

#print(my_func(2, 3))

def my_func(a, n):
       res = 1
       for i in range(abs(n)):
              res *= a
       return 1 / res


print(my_func(float(input("Введите положительное число для возведения в степень")),
              int(input("Введите целое отрицательное число"))))
