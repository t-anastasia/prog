"""
Терентьева Анастасия Максимовна, 3пг
Площадь треугольника через Формулу Герона
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
S = 0
p = 0

p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print("S = ", S)

input()