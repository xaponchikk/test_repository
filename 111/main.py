# a = int(input("Введите числовой диапозон от: "))
# b = int(input("Введите числовой диапозон от: "))
#
# otv = 0
# a = a - 1
#
# while a != b:
#     a += 1
#     otv += a
#
# print(otv)

import random

ch = 2

dict = {1: "zzz", 2: "xxx", 3: "ccc"}

for key in dict:
    if ch == key:
        dict[key] = random.choice(dict)
        print()


#n = dict.values()
#print(n)
#x = random.choice(n)
#print(dict[x])

print(dict)
