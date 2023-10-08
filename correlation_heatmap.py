#Machine learning project 1: PCA and data visualization
#Author: Bertram Hage, Markus Kaad, Simen Fjeld
#Date: October 3, 2023
#Description: This script computes a correlation matrix of the standardized attributes then creates a heatmap displaying the correlation.

from load_data import *
import matplotlib.pyplot as plt
import seaborn as sns

# Standardization
Y = (X - X.mean(axis = 0))/X.std(axis=0)

corrMatrix = np.corrcoef(X, rowvar=False)
corrMatrix_rounded = np.around(corrMatrix, 2)

ax = plt.axes([0.15, 0.15, 0.8, 0.8])

hm = sns.heatmap(data=corrMatrix_rounded, cmap="coolwarm", xticklabels=attributeNames, yticklabels=attributeNames,
                annot=True, ax=ax)

plt.title('Correlation Heatmap')
plt.figure(figsize=(10, 8))

hm.set_xticklabels(hm.get_xticklabels(), rotation=45, ha='right')

plt.show()
