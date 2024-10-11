import numpy as np

# Define matrix A and vector c
A = np.array([[2, 4, -2],
              [4, 9, -3],
              [-2, -1, 7]])
c = np.array([4, 8, -6])

# Function to perform LU decomposition without pivoting
def lu_decomposition_no_pivot(A):
    n = A.shape[0]
    L = np.eye(n)  # Initialize L as identity matrix
    U = A.copy().astype(float)  # Initialize U as a copy of A

    # Perform the LU decomposition
    for i in range(n):
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, :] = U[j, :] - factor * U[i, :]
    
    return L, U

# Perform LU decomposition
L, U = lu_decomposition_no_pivot(A)

# Print LU factorization results
print("Matrix A:")
print(A)

print("\nLower triangular matrix L:")
print(L)

print("\nUpper triangular matrix U:")
print(U)

# Step 2: Solve Lz = c using forward substitution
z = np.linalg.solve(L, c)
print("\nSolution to Lz = c (z):")
print(z)

# Step 3: Solve Uy = z using backward substitution
y = np.linalg.solve(U, z)
print("\nSolution to Uy = z (y):")
print(y)


#Entire solut!!!ion without refatoring and pivoting