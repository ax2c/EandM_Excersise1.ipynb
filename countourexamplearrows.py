###################################################
# Example of filled contour plotting #
# #
# Eric Leibensperger - 08/31/2020 (python version)#
# Based upon MATLAB routines by created by #
# Bruce Thompson (08/20/2004) & edited by #
# Kelley Sullivan (09/04/2011) #
# #
# Example executed by: #
# (Andrew Coit 09/05/2026) #
###################################################
# Bring the following packages in to help with math and plotting
import numpy as np
import matplotlib.pyplot as plt
# Create coordinates in x, y directions that go from
# -5 --> +5 and have 11 points… [-5,-4,-3,-2,-1,0,1,2,3,4,5]
# numpy’s linspace function accepts the lowest value (-5),
# highest value (5), and the number of desired points (11)
xCoord = np.linspace(-5.0, 5.0, 11)
yCoord = np.linspace(-5.0, 5.0, 11)
# Create a 2D mesh of these values. This is like setting out a
# 2D grid. Each location has an x value and a y value. X and Y
# are thus 2D. For X, each column is the same value. For Y,
# each row has the same value
#
# For example, X looks like this:
# [[-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.],
# [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.]]
# numpy’s meshgrid accepts the x and y values and fill in.
X, Y = np.meshgrid(xCoord, yCoord)
# Calculate the function Z = -0.5X^2 + XY + Y^2
# ** = ^ in python. No need for special matrix multiplication
# here. Note that this is calculated at each and every point or
# 11 x 11 = 121 locations. Z is 11x11 in size (like X and Y!)
Z = -0.5*X ** 2 + X*Y + Y ** 2
# Open up a window to add graphics. Use the figure() from
# matplotlib.pyplot
plt.figure()
# Contour levels for the graph. Linspace like above.
# Note that I manually found the range; this should be edited
# if the range changes or if something more elegant is desired
# … for example, finding the min and max
levels = np.linspace(-40,40,17)
# Create the contour plot, having contours colored black ('k')
contour = plt.contour(X, Y, Z, levels, colors='k')
# Add black contour labels, 12pt font and force 1 decimal place
plt.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=12)
# Add the filled contour on top, using the shades of blue into
# white into red as the colormap.
contour_filled = plt.contourf(X, Y, Z, levels,cmap='viridis')
#Calculate the gradient and plot its components as a vector
# field on top of filled contour
dZdY,dZdX = np.gradient(Z) # Note that the order of the
# output is Y,X (opposite of
# meshgrid)
# Add gradient vectors to our graph
plt.quiver(X,Y,dZdX,dZdY)
# Add the colorbar for reference
plt.colorbar(contour_filled)
# Add a title, x-axis label, and y-axis label to the graph
plt.title('My graph')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
# Show the plot to the world!
plt.show()