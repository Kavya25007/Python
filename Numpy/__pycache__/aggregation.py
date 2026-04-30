import numpy as np

# 1D Array
arr = np.array([10, 20, 30, 40])

print("Array:", arr)

# Basic Aggregations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))

# Other Aggregations
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Product:", np.prod(arr))

# -----------------------------

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("\n2D Array:\n", arr2)

# Axis = 0 (Column-wise)
print("Column-wise Sum:", np.sum(arr2, axis=0))
print("Column-wise Mean:", np.mean(arr2, axis=0))

# Axis = 1 (Row-wise)
print("Row-wise Sum:", np.sum(arr2, axis=1))
print("Row-wise Mean:", np.mean(arr2, axis=1))

# -----------------------------

# Using array methods
print("\nUsing Methods:")
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())