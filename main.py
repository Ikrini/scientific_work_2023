import math
from photon import *
import json
import random
from array import *
import matplotlib.pyplot as plt

import numpy as np
import math
import random
import vox
#import test2

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

photon = Photon(0.15, 10, 0.8, 100, 0, 0, 1, 100000, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0.15, 0.15, 0, 0, 0, 0, 101, 0)

#snells_res = photon.snells_low(30, 0, 1, 1.33)
#print(photon.current_orient(current={'x': 0, 'y': 0, 'z': 5}))

#print(list(range(photon.count)))
#print(photon.show_vars())
boundary = photon.boundary
#voxels = photon.bulk(10) / photon.split_voxels()
#print(voxels)
left = -(boundary/2)
right = boundary/2

array_current = []
nn = 10

voksels = 100
voksel = boundary / voksels
array_voksel = []

for x in range(boundary):
    for y in range(boundary):
        for z in range(boundary):
            array_voksel.append([x - boundary / 2, y - boundary / 2, z, 0])

for i in range(photon.count):
    current = photon.current_orient(current={'x': 0, 'y': 0, 'z': 0})
    direction = photon.direction_orient(direction={'x': 0, 'y': 0, 'z': 1})
    #w = photon.w
    w = 1
    #x = np.empty((101, 101, 101))
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
            #print(f"photon was absorbed | weight of the photon = {w}")
            break

        array_current.append({'x': current['x'], 'y': current['y'], 'z': current['z'], 'w': w})
        #print(array_current, '\n')

for i in range(len(array_voksel)):
    for f in range(len(array_current)):
        if (math.floor(array_current[f]['x']) == array_voksel[i][0] and
                math.floor(array_current[f]['y']) == array_voksel[i][1] and
                math.floor(array_current[f]['z']) == array_voksel[i][2]):
            array_voksel[i][3] += array_current[f]['w']

for i in range(len(array_voksel)):
    if (array_voksel[i][3] != 0):
        print(array_voksel[i])

def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e

# build up the numpy logo
n_voxels = np.zeros((nn, nn, nn), dtype=bool)
#print(n_voxels)
for i in range(len(array_voksel)):
        if (array_voksel[i][3] != 0):
            n_voxels[int(array_voksel[i][3]), int(array_voksel[i][3]),
                     int(array_voksel[i][3])] = True
            print(array_voksel[i][3])

#n_voxels[1, 0, 0] = True

# Control Transparency
alpha = 0.9
#colors = np.empty(n_voxels, dtype=np.float32)
#colors[0] = [1, 0, 0, alpha]
facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
filled = np.ones(n_voxels.shape)

# upscale the above voxel image, leaving gaps
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)

# Shrink the gaps
x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
#print(x,y,z)
x[0::2, :, :] += 0.95
y[:, 0::2, :] += 0.95
z[:, :, 0::2] += 0.95

#---------
#size of the voxels
#x[1::2, :, :] += 0.1
#y[:, 1::2, :] += 0.1
#z[:, :, 1::2] += 0.1



#---------

#x[1::2, :, :] += 0.95
#y[:, 1::2, :] += 0.95
#z[:, :, 1::2] += 0.95

fig = plt.figure()

ax = fig.add_subplot(projection='3d')
#ax.set_xlim(-5,5)
#ax.set_ylim(-5,5)
#ax.set_zlim(-5,5)
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)

plt.show()
























