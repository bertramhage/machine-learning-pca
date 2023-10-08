#Machine learning project 1: PCA and data visualization
#Author: Bertram Hage, Markus Kaad, Simen Fjeld
#Date: October 3, 2023
#Description: This script performs a PCA by computing SVD then creates boxplots of the data projected onto the first 3 principal components.

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

# Find unique values in y
unique_values_y = np.unique(y)

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
axs[1].set_title('PCA boxplots')

# Plot PC{i} vs. class for i=0, i=1, i=2
for i in range(3):
    zi_lists = [[] for _ in range(1, len(unique_values_y) + 1)]
    for j, unique_val in enumerate(unique_values_y):
        indices = [index for index, val in enumerate(y) if val == unique_val]
        zi_lists[j] = [Z[:, i][index] for index in indices]
    axs[i].boxplot(zi_lists, vert=False, showfliers=False)
    axs[i].set_xlabel('PC{0}'.format(i + 1))

# Set y-axis labels to class names for the first subplot
axs[0].set_yticks(range(1, len(classNames)+1))
axs[0].set_yticklabels(classNames)
axs[0].set_ylabel('Class')

plt.tight_layout()
plt.show()
