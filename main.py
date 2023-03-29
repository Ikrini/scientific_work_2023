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

photon = Photon(0.15, 10, 0.8, 100, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0.15, 0.15, 0, 0, 0, 0, 101, 0)

#snells_res = photon.snells_low(30, 0, 1, 1.33)
#print(photon.current_orient(current={'x': 0, 'y': 0, 'z': 5}))

#print(list(range(photon.count)))
#print(photon.show_vars())
boundary = photon.boundary
voxels = photon.bulk(10) / photon.split_voxels()
atot = photon.atot
#print(voxels)
left = -(boundary/2)
right = boundary/2

for i in range(photon.count):
    current = photon.current_orient(current={'x': 0, 'y': 0, 'z': 0})
    direction = photon.direction_orient(direction={'x': 0, 'y': 0, 'z': 1})
    #w = photon.w
    w = 1
    x = np.empty((101, 101, 101))
    for binx in range(photon.N):
        y = []
        for biny in range(photon.N):
            z = []
            for binz in range(photon.N):
                while(left <= current['x'] < right and left <= current['y'] < right and 0 <= current['z'] < boundary):
                    [teta, fi] = photon.angles_direction()
                    direction = photon.photons_direction(direction, teta, fi)
                    l_run = photon.free_run()
                    w = photon.weight(w, l_run)
                    new_current = photon.change_orient(current, l_run, direction)
                    current['x'] += new_current['x']
                    current['y'] += new_current['y']
                    current['z'] += new_current['z']
                    print(current, f"\t\t\t\t weight = {w} photon = {i}")
                    #print(direction, f"\t\t\t\t weight = {w} photon = {i}")
                    #atot = photon.atot
                    if w <= 0.0001:
                        print(f"photon was absorbed | weight of the photon = {w}")
                        break
                    # Drop photon weight (W) into local bin
                    delta_w = (w * photon.mua) / (photon.mua + photon.mut)
                    absorb = w * (1 - photon.albedo)    #photon weight absorbed at this step
                    #w -= absorb                         #decrement WEIGHT by amount absorbed
                    #atot += absorb                      #accumulate absorbed photon weight

                    #deposit power in cube coordinates x,y,z

                    nx = math.floor((current['x'] / boundary) * photon.NX)  # индекс массива, заполняю как тек.коор-та...
                    ny = math.floor((current['y'] / boundary) * photon.NY) #TODO где эта формула должна находиться ?
                    nz = math.floor((current['z'] / boundary) * photon.NZ)

                    print("delta_w = ", delta_w)
                    x[binx][biny][binz]+= delta_w                         #TODO заполняет только первый элемент


                    #x = {nx: atot}
                    #y = {ny: atot}
                    #z = {nz: atot}
                    #r = math.sqrt(current['x'] * current['x'] + current['y'] * current['y'])        #current cylindrical radial position
                    #print("delta_w = ", delta_w)
                    #print("x,y,z = ", x,y,z)
                    print(x.reshape(101,101,101))                                                                #TODO какую итерацию рассчёта тек.коор-ат класть в массив (в ячейку) ?





x = {1: "dwe"}
y = {1: "dwe"}
z = {1: "dwe"}























