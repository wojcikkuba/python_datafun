from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = Axes3D(fig, azim=-128, elev=43)
s = .05
X = np.arange(-2, 2.+s, s)
Y = np.arange(-1, 3.+s, s)
X, Y = np.meshgrid(X, Y)
Z = (1.-X)**2 + 100.*(Y-X*X)**2
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, norm=LogNorm(), cmap='gist_rainbow')

plt.xlabel("x")
plt.ylabel("y")

plt.show()
