# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.



numbers_1 = set(input('Введите элементы первого множества через пробел ').split())
numbers_2 = set(input('Введите элементы второго множества через пробел ').split())
list_1 = [*numbers_1, *numbers_2]
sort = []
for num in list_1:
    sort.append(int(num))
sort.sort()

print(sort)
# sorted = []
# for num in numbers_1:
#     sorted.append(num)
# # for num in numbers_2:
# #     sorted.append(num)
# sorted.sort
# print(sorted)



















# # amount_1 = int(input('Введите количество элементов первого множества '))
# # amount_2 = int(input('Введите количество элементов второго множества '))
# numbers_1 = (input('Введите элементы первого множества через пробел '))
# numbers_2 = (input('Введите элементы второго множества через пробел '))
# num_1 = numbers_1.split()
# num_2 = numbers_2.split()
# result = []
# # numbers_1 = set()
# # nu2mbers_ = set()
# # numbers = {"",}
# # amount_1, amount_2 = amount_1.set(), amount_2.set()
# # numbers_1_total = numbers_1.split()
# # numbers_2_total = numbers_2.split()
# # for num in numbers_1 and numbers_2:
# #     numbers.add.num
# for num in num_1:
#     result.append(num)
# for num in num_2:
#         result.append(num)
# print(result)    
