import math
from photon import *
import json
import random
from array import *

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

photon = Photon(0.15, 10, 0.8, 3, 0, 0, 1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0.15, 0, 0, 0, 0, 0, 0)

#snells_res = photon.snells_low(30, 0, 1, 1.33)
#print(photon.current_orient(current={'x': 0, 'y': 0, 'z': 5}))

#print(list(range(photon.count)))
#print(photon.show_vars())
boundary = photon.boundary
voxels = photon.bulk() / photon.split_voxels()
#print(voxels)

for i in range(photon.count):
    current = photon.current_orient(current={'x': 0, 'y': 0, 'z': 0})
    direction = photon.direction_orient(direction={'x': 0, 'y': 0, 'z': 1})
    #w = photon.w
    w = 1
    while(0 <= current['x'] < boundary and 0 <= current['y'] < boundary and 0 <= current['z'] < boundary):
        [teta, fi] = photon.angles_direction()
        direction = photon.photons_direction(direction, teta, fi)
        l_run = photon.free_run()
        #weight = photon.weight()
        w = photon.weight(w, l_run)
        #current['x'] += 1
        new_current = photon.change_orient(current, l_run, direction)
        current['x'] += new_current['x']
        current['y'] += new_current['y']
        current['z'] += new_current['z']
        # print(current, f"\t\t\t\t weight = {w} photon = {i}")


        atot = photon.atot
        nr = photon.nr
        nz = photon.nz
        #f = photon.f
        f = [[0 for ii in range(nr)] for jj in range(nz)]
        dz = photon.dz

        for j in range(nr):
            for z in range(nz):
                f[0][0] = 0
#        """считаем вес фотона на каждом вокселе (собираем чтобы потом положить в воксель)"""
                absorb = w * (1 - photon.albedo)
                w -= absorb
                #atot += absorb
#                """кладём вес фотона в воксель [ir][iz]"""
                r = math.sqrt(current['x'] * current['x'] + current['y'] * current['y'])
                #ir = (r / photon.dr) + 1
                #iz = (abs(current['z']) / dz) + 1
                if j >= nr:
                    j = nr
                if z >= nz:
                    z = nz
                #print([ir],[iz], end=' ')
                f[j][z] += absorb
                print(f[j][z], end='\n')


        if w <= 0.0001:
           # print(f"photon was absorbed | weight of the photon = {w}")
            break































