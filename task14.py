# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.


N = int(input("Введите число N: "))
k = 0
power_2 = 1

while power_2 <= N:
    print(power_2)
    k += 1
    power_2 = 2 ** k
