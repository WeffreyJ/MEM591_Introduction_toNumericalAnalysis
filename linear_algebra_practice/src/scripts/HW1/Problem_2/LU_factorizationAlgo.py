import numpy as np

# Helper Functions for Row Operations (as used earlier)
def RowAdd(A, k, l, scale):
    """
    Adds a scaled version of row k to row l in matrix A.
    The function modifies row l by adding 'scale' times row k.
    """
    B = np.copy(A).astype('float64')
    B[l, :] += B[k, :] * scale  # Adding scaled row k to row l
    return B

# LU Factorization function with Partial Pivoting (Doolittle’s Method)
def lu_factorization_with_pivoting(A):
    """
    Performs LU factorization with partial pivoting.
    Returns permutation matrix P, lower triangular matrix L, and upper triangular matrix U 
    such that PA = LU.
    """
    n = A.shape[0]
    L = np.eye(n)  # Initialize L as an identity matrix
    U = np.copy(A).astype('float64')  # Initialize U as a copy of A
    P = np.eye(n)  # Permutation matrix
    
    for i in range(n):
        # Partial pivoting: Find the row with the largest pivot element
        max_row = np.argmax(np.abs(U[i:, i])) + i
        if max_row != i:
            # Swap rows in U and P
            U[[i, max_row]] = U[[max_row, i]]
            P[[i, max_row]] = P[[max_row, i]]
            L[[i, max_row], :i] = L[[max_row, i], :i]  # Swap the rows in L up to the i-th column
        
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor  # Store the factor in L
            U[j, :] -= factor * U[i, :]
    
    return P, L, U

# Forward substitution for Lz = Pb
def forward_substitution(L, b):
    """
    Solves Lz = b using forward substitution, where L is a lower triangular matrix.
    """
    n = len(b)
    z = np.zeros(n)
    
    for i in range(n):
        z[i] = (b[i] - np.dot(L[i, :i], z[:i]))
    
    return z

# Back substitution for Uy = z
def back_substitution(U, z):
    """
    Performs back substitution to solve an upper triangular system Uy = z.
    Returns the solution vector y.
    """
    n = U.shape[0]
    y = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        y[i] = (z[i] - np.dot(U[i, i+1:], y[i+1:])) / U[i, i]
    
    return y

# Part (a) - Solve Ax = b using LU factorization with pivoting
A = np.array([[2, 4, -2],
              [4, 9, -3],
              [-2, -1, 7]])
b = np.array([2, 8, 10])

# Solve using LU factorization with pivoting
P, L, U = lu_factorization_with_pivoting(A)

print("Permutation matrix P:\n", P)
print("Lower triangular matrix L:\n", L)
print("Upper triangular matrix U:\n", U)

# Step 1: Solve Lz = Pb using forward substitution
Pb = np.dot(P, b)
z = forward_substitution(L, Pb)
print("Solution z from Lz = Pb: ", z)

# Step 2: Solve Uy = z using back substitution
y = back_substitution(U, z)
print("Solution y from Uy = z: ", y)

# Part (b) - Solving Ay = c using LU Factorization

# Matrix c for the second system
c = np.array([4, 8, -6])

# Step 1: Solve Lz = Pc using forward substitution
Pc = np.dot(P, c)
z_c = forward_substitution(L, Pc)
print("Solution z from Lz = Pc: ", z_c)

# Step 2: Solve Uy = z using back substitution
y_c = back_substitution(U, z_c)
print("Solution y from Uy = z: ", y_c)

##
# 
# ## 3 Ways to actually check if my solutions are correct, Let's see
# Verify if A ≈ L * U
A_reconstructed = np.dot(L, U)

print("Original matrix A:\n", A)
print("Reconstructed matrix L * U:\n", A_reconstructed)

# Check if the original matrix A is close to the reconstructed matrix L * U
if np.allclose(A, A_reconstructed):
    print("LU factorization is correct.")
else:
    print("LU factorization is incorrect.")


# sSecond Method of checking
# Step 3: Multiply A by the solution y (or x) and compare with b
b_computed = np.dot(A, y)

print("Original b: ", b)
print("Computed b from A * y: ", b_computed)

# Check if the computed b is close to the original b
if np.allclose(b, b_computed):
    print("The solution is correct.")
else:
    print("The solution is incorrect.")



#Third way of checking

from scipy.linalg import lu

# Get LU factorization using scipy
P, L_scipy, U_scipy = lu(A)

# Compare L and U with those from scipy's LU decomposition
print("L from scipy:\n", L_scipy)
print("U from scipy:\n", U_scipy)

# Check if the L and U matrices are close to those obtained manually
if np.allclose(L, L_scipy) and np.allclose(U, U_scipy):
    print("LU factorization matches scipy's results.")
else:
    print("LU factorization does not match scipy's results.")






