# :  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите числоа а: '))
b = int(input('Введите числоа b: '))
def mod(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return mod(a*a, b//2)
    else:
        return a * mod(a*a, (b-1)//2)
print(mod(a,b))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.