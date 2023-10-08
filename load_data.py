#Machine learning project 1: PCA and data visualization
#Author: Bertram Hage, Markus Kaad, Simen Fjeld
#Date: October 3, 2023
#Description: This scrips loads data from an xls file and organizes attibute and class data into numpy arrays.

import numpy as np
import xlrd

# Load xls sheet with data
doc = xlrd.open_workbook('Dry_Bean_Dataset.xls').sheet_by_index(0)

# Extract attribute names (1st row, column 1 to 16)
attributeNames = doc.row_values(0, 0, 16)

# Extract class names to python list,
# then encode with integers (dict)
classLabels = doc.col_values(16, 1, 13612)
classNames = sorted(set(classLabels))
classDict = dict(zip(classNames, range(7)))

# Extract vector y, convert to NumPy array
y = np.asarray([classDict[value] for value in classLabels])

# Preallocate memory, then extract excel data to matrix X
X = np.empty((13611, 16))
for i, col_id in enumerate(range(0, 16)):
    X[:, i] = np.asarray(doc.col_values(col_id, 1, 13612))

# Compute values of N, M and C.
N = len(y)
M = len(attributeNames)
C = len(classNames)

print('Data loaded')