"""
Терентьева Анастасия Максимовна, 3пг

2.6. Перепишите лямбда-функцию, генерирующую квадраты чисел из
переменной типа list, через генератор списка.

"""

list = [1,2,3,4,5,6,7,8,9,10]

sq_list = [(lambda x: x ** 2)(item) for item in list]

print(sq_list)