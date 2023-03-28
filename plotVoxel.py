# Import all the necessary libraries and packages in the code
import matplotlib.pyplot as plt
import numpy as np
# Defining the user-defined cubes() function
def cubes(side):
    # задаём размер оси
    x, y, z = np.indices((10 10, 10))
    # длина стороны куба
    cube = (x < side) & (y < side) & (z < side)
    # форма
    voxelarray = cube
    # цвет вокселей
    colors = np.empty(voxelarray.shape, dtype=object)
    # цвет куба
    colors[cube] = 'green'
    # оси
    ax = plt.figure(figsize=(10, 10)).add_subplot(projection='3d')
    # построение куба
    ax.voxels(voxelarray , facecolors=colors, edgecolor='k')
    # загаловок
    plt.title("Трёхмерный куб разбитый на воксели")
    # показать заголовок
    plt.show()


def main():
    # размер куба
    sides = 9
    cubes(sides)
if __name__ == "__main__":
    main ()