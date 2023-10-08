#Machine learning project 1: PCA and data visualization
#Author: Bertram Hage, Markus Kaad, Simen Fjeld
#Date: October 3, 2023
#Description: This script performs a PCA by computing SVD then creates a bar graph displaying the coefficients of the attributes to the first 3 principal components

from load_data import *
import matplotlib.pyplot as plt
from scipy.linalg import svd

# Standardize data
Y = X - np.ones((N,1))*X.mean(0)
Y = Y / np.std(Y, axis=0)

# PCA by computing SVD of Y
U,S,Vh = svd(Y,full_matrices=False)
V=Vh.T
N,M = X.shape

# Principal components to include
pcs = [0, 1, 2]

legendStrs = ['PC' + str(e + 1) for e in pcs]
c = ['r', 'g', 'b']
bw = 0.2
r = np.arange(1, M + 1)

for i in pcs:
    plt.barh(r + i * bw, V[:, i], height=bw)

plt.yticks(r + bw * len(pcs) / 2, attributeNames)
plt.ylabel('Attributes')
plt.xlabel('Component coefficients')
plt.legend(legendStrs)
plt.grid()
plt.title('PCA component coefficients for bean data')
plt.show()