import math
from photon import *

import numpy as np
import math
import random

#a, b = map(int, input().split())
#print(math.sqrt((a**2)+(b**2)))

#n, k = map(int, input().split())
#print(math.factorial(n) / (math.factorial(k)* math.factorial(n-k)))

#n, m = map(int, input().split())
#group = n/m
#print(math.ceil(20/group))

#a, b = 1, 2
#print(a, b, sep=" | ")
#print("turtle", end=" ")
#print(f"i test var {a}; and {b} printing")

#a = float(input("enter symbols for printing: "))

#round(math.pi,3) accuracy untill 3 float sign after comma

"""
Для определения глубины флуорофора:
1) нужно промоделировать расположение флуорофора на разных глубинах для длин волн 405 и 660 нм
2) нужно рассчитать, какое количество фотонов выходит назад из среды на каждой длине волны
3) построить зависимость отношения сигналов (числа фотонов) на разных длинах волн от глубины
"""

photon = Photon(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

snells_res = photon.snells_low(30, 0, 1, 1.33)
print(snells_res)
print(photon.at)
print(photon.show_vars())























