import numpy as np

# 1D Arrays
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Array a:", a)
print("Array b:", b)

# -----------------------------
# 🔹 Arithmetic Operations
print("\n--- Arithmetic ---")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** 2 =", a ** 2)
print("a % 3 =", a % 3)
print("a // 2 =", a // 2)

# -----------------------------
# 🔹 Scalar Operations
print("\n--- Scalar ---")
print("a + 5 =", a + 5)
print("a * 2 =", a * 2)

# -----------------------------
# 🔹 Universal Functions (ufuncs)
print("\n--- Functions ---")
print("sqrt(a) =", np.sqrt(a))
print("log(a) =", np.log(a))
print("exp(a) =", np.exp(a))
print("sin(a) =", np.sin(a))

# -----------------------------
# 🔹 Comparison Operations
print("\n--- Comparison ---")
print("a > 15 =", a > 15)
print("a == 20 =", a == 20)

# -----------------------------
# 🔹 Logical Operations
print("\n--- Logical ---")
print("AND =", np.logical_and(a > 10, a < 30))
print("OR =", np.logical_or(a > 20, a < 15))

# -----------------------------
# 🔹 2D Arrays (Matrix Operations)

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

print("\n--- Matrix Operations ---")
print("A + B =\n", A + B)        # element-wise
print("A * B =\n", A * B)        # element-wise
print("A @ B =\n", A @ B)        # matrix multiplication
print("dot(A, B) =\n", np.dot(A, B))

# -----------------------------
# 🔹 Aggregation (quick add-on)
print("\n--- Aggregation ---")
print("Sum =", np.sum(a))
print("Mean =", np.mean(a))