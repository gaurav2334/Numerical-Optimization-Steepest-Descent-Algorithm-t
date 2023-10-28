#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

import matplotlib.pyplot as plt

# Create a grid of x and y values
x = np.linspace(-2.5, 2.5, 1001)
y = np.linspace(-2, 2, 1001)
X, Y = np.meshgrid(x, y)

# Define the function to plot
Z = (X*np.exp(-X**2 - Y**2))

# Create the contour plot
plt.contour(X, Y, Z, 10)

# Add a color bar
plt.colorbar()

# Add axis labels and a title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour plot of exp(x-(x^2 + y^2))')

# Show the plot
plt.show()


# In[31]:


from mpl_toolkits.mplot3d import Axes3D  
import random

def fun(x, y):
    return X*np.exp(-X**2 - Y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-2.5, 2.5, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array(fun(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

