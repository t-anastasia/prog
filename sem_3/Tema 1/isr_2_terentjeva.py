"""
Терентьева Анастасия Максимовна, 3пг
Сумма первых n-членов арифметической прогрессии
"""

S = 0
n = int(input("Enter n: ")) # номер
a1 = int(input("Enter a1: ")) # первый член
p = str(input("Do you have d? (yes/no)")) # разность

if p == 'yes':
    d = int(input("Enter d: "))
    S = (n * (2 * a1 + d * (n - 1))) / 2
    print("Summa = ", S)

else:
    an = int(input("Enter an: "))
    S = (n * (a1 + an)) / 2
    print("Sum = ", S)

input("Click 'Enter'")