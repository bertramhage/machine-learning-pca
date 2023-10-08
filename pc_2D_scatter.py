#Machine learning project 1: PCA and data visualization
#Author: Bertram Hage, Markus Kaad, Simen Fjeld
#Date: October 3, 2023
#Description: This script performs a PCA by computing SVD then creates a 2D scatter plot of the data projected onto the i'th and j'th principal component space.

from load_data import *
import matplotlib.pyplot as plt
from scipy.linalg import svd

# Standardize data
Y = X - np.ones((N,1))*X.mean(0)
Y = Y / np.std(Y, axis=0)

# PCA by computing SVD of Y
U,S,Vh = svd(Y,full_matrices=False)
V = Vh.T    

# Project the centered data onto principal component space
Z = Y @ V

# Indices of the principal components to be plotted
i = 0
j = 1

# Plot PCA of the data
for c in range(C):
    class_mask = y==c
    plt.plot(Z[class_mask,i], Z[class_mask,j], 'o', alpha=.5)
plt.title('PCA scatter')
plt.legend(classNames, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=7)
plt.xlabel('PC{0}'.format(i+1))
plt.ylabel('PC{0}'.format(j+1))

plt.show()