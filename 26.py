# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def rec_pow(a, b):
    if b == 0:
        return 1
    else:
        return a * rec_pow(a, b-1)


A = int(input("А: "))
B = int(input("B: "))

print(rec_pow(A, B))
