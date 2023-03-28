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

photon = Photon(0.15, 10, 0.8, 100, 0, 0, 1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0.15, 0.15, 0, 0, 0, 0, 0, 0)

#snells_res = photon.snells_low(30, 0, 1, 1.33)
#print(photon.current_orient(current={'x': 0, 'y': 0, 'z': 5}))

#print(list(range(photon.count)))
#print(photon.show_vars())
boundary = photon.boundary
voxels = photon.bulk(10) / photon.split_voxels()
atot = photon.atot
#print(voxels)

for i in range(photon.count):
    current = photon.current_orient(current={'x': 50, 'y': 50, 'z': 0})
    direction = photon.direction_orient(direction={'x': 0, 'y': 0, 'z': 1})
    #w = photon.w
    w = 1
    while(0 <= current['x'] < boundary and 0 <= current['y'] < boundary and 0 <= current['z'] < boundary):
        [teta, fi] = photon.angles_direction()
        direction = photon.photons_direction(direction, teta, fi)
        l_run = photon.free_run()
        w = photon.weight(w, l_run)
        new_current = photon.change_orient(current, l_run, direction)
        #x, y, z = [photon.count], [photon.count], [photon.count]
        current['x'] += new_current['x']
        current['y'] += new_current['y']
        current['z'] += new_current['z']
        #x[i] = math.floor(current['x'])
        #y[i] = math.floor(current['y'])
        #z[i] = math.floor(current['z'])
        print(current, f"\t\t\t\t weight = {w} photon = {i}")
        #atot = photon.atot

        if w <= 0.0001:
           # print(f"photon was absorbed | weight of the photon = {w}")
            break
#Drop photon weight (W) into local bin
        absorb = w * (1 - photon.albedo)    #photon weight absorbed at this step
        w -= absorb                         #decrement WEIGHT by amount absorbed
        atot += absorb                      #accumulate absorbed photon weight
#deposit power in cube coordinates x,y,z
        #nx = math.floor((current['x'] / max(x))*photon.NX)       #индекс массива, заполняю как тек.коор-та...
        #ny = math.floor((current['y'] / max(y)) * photon.NY)
        #nz = math.floor((current['z'] / max(z)) * photon.NZ)
        r = math.sqrt(current['x'] * current['x'] + current['y'] * current['y'])        #current cylindrical radial position
        print("r is ", r)
        ix = (r / photon.dx) + 1
        iy = (r / photon.dy) + 1
        iz = (math.fabs(current['z']) / photon.dz) + 1
        print("ix, iy, iz is ", ix, iy, iz)
        if ix >= photon.NX:
            ix = photon.NX
        if iy >= photon.NY:
            iy = photon.NX
        if iz >= photon.NZ:
            iy = photon.NZ



























