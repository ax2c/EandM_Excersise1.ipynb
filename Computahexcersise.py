import numpy as np
import matplotlib.pyplot as plt
xCoord = np.linspace(-8.0, 2.0, 100)
yCoord = np.linspace(-7.0, 3.0, 100)
# this was to set up the plotting and the 2d grid space.
X, Y = np.meshgrid(xCoord, yCoord)
#south hill height function
Z = 10 * (2 * X * Y - 3 * X**2 - 4 * Y**2 - 18 * X + 28 * Y + 12)
#This next one builds the figure
plt.figure()
levels = np.linspace(np.min(Z), np.max(Z), 21)

contour = plt.contour(X, Y, Z, levels, colors='k')
plt.clabel(contour, colors='k', fmt='%2.1f', fontsize=12)

contour_filled = plt.contourf(X, Y, Z, levels, cmap='BrBG_r')
plt.colorbar(contour_filled)

#vector field
dZdY, dZdX = np.gradient(Z)
plt.quiver(X, Y, dZdX, dZdY)

plt.title('South Hill Contours and Gradients')
plt.xlabel('x (miles)')
plt.ylabel('y (miles)')
plt.show()

#for my final trick it becomes 3d
#ALSO ALSO ALSO the flat map shows up first so just be sure to exit out that one to see the 3d.

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='BrBG_r')
ax.set_zlabel('z (feet)')

plt.colorbar(surf, shrink=0.5, aspect=5)
plt.xlabel('x (miles)')
plt.ylabel('y (miles)')
plt.title('South Hill 3D Surface Plot')
plt.show()

