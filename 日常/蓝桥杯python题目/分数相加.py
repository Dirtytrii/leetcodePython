import math

son = 1
mother = 1
plus_son = 2
plus_mo = 2

for _ in range(0, 19):
    son = son + plus_son
    mother = mother * plus_mo
    plus_son *= 2

temp = math.gcd(son, mother)
print(temp)

print(son / temp, end='/')
print(mother / temp)
