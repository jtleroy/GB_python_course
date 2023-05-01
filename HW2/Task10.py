# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input("Укажите количество монет на столе: "))
array = [0] * n

i = 0
while i < n:
    array[i] = random.randint(0, 1)
    i = i + 1
# print(array[0], array[1], array[2], array[3], array[4])
string = ""
for coin in array:
    string = string + str(coin) + " "
print(string)

unos = 0
for coin in array:
    if coin == 1:
        unos = unos + 1
ceros = n - unos
if unos > ceros:
    print("Минимальное количество монет, которые нужно перевернуть: ", ceros)
else:
    print("Минимальное количество монет, которые нужно перевернуть: ", unos)
