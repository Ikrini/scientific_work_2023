import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

df = pd.DataFrame({"x": [14630, 14630, 14360, 14360, 14360], "y": [21750, 21770, 21790, 21930, 21950],
                   "z": [4690, 4690, 4690, 5290, 5270]})


def get_cube():
    phi = np.arange(1, 10, 2) * np.pi / 4
    Phi, Theta = np.meshgrid(phi, phi)

    x = np.cos(Phi) * np.sin(Theta)
    y = np.sin(Phi) * np.sin(Theta)
    z = np.cos(Theta) / np.sqrt(2)
    return x, y, z


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
L = 10

for i in df.index:
    x, y, z = get_cube()

    # Change the centroid of the cube from zero to values in data frame
    x = x * L + df.x[i]
    y = y * L + df.y[i]
    z = z * L + df.z[i]
    ax.plot_surface(x, y, z)
    ax.set_zlabel("z")

plt.xlabel("x")
plt.ylabel("y")
plt.show()