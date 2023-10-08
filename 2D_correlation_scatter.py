#Machine learning project 1: PCA and data visualization
#Author: Bertram Hage, Markus Kaad, Simen Fjeld
#Date: October 3, 2023
#Description: This scripts creates a 2D scatter plot of the i'th and j'th attribute against each other.

# Imports the numpy and xlrd package, then runs the load data code
from load_data import *
import matplotlib.pyplot as plt

# Data attributes to be plotted
i = 0
j = 4

# Make a plot of the i'th attribute against the j'th attribute
f = plt.figure()
plt.title('Corrrelation scatter')

for c in range(C):
    # select indices belonging to class c:
    class_mask = y==c
    plt.plot(X[class_mask,i], X[class_mask,j], 'o',alpha=.3)

plt.legend(classNames)
plt.xlabel(attributeNames[i])
plt.ylabel(attributeNames[j])

plt.show()