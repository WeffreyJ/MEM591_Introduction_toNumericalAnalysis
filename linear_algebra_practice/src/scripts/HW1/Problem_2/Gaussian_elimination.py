import numpy as np

# Helper Functions for Gaussian Elimination
def RowSwap(A, k, l):
    """
    Swaps rows k and l of matrix A.
    A is a NumPy array, and it returns a new array with rows k and l swapped.
    """
    B = np.copy(A).astype('float64')
    B[[k, l]] = B[[l, k]]  # Swapping rows directly using NumPy
    return B

def RowScale(A, k, scale):
    """
    Scales row k of matrix A by the given scalar 'scale'.
    """
    B = np.copy(A).astype('float64')
    B[k, :] *= scale  # Multiplying the entire row by the scale
    return B

def RowAdd(A, k, l, scale):
    """
    Adds a scaled version of row k to row l in matrix A.
    The function modifies row l by adding 'scale' times row k.
    """
    B = np.copy(A).astype('float64')
    B[l, :] += B[k, :] * scale  # Adding scaled row k to row l
    return B

def find_pivot(A, row):
    """
    Performs partial pivoting by finding the row with the largest absolute value
    in the current column and swaps it with the current row.
    """
    max_row = np.argmax(np.abs(A[row:, row])) + row
    if max_row != row:
        A = RowSwap(A, row, max_row)  # Swap the current row with the row having max pivot
    return A

import numpy as np

# Gaussian elimination function (as before)
def gaussian_elimination(A):
    n = A.shape[0]
    U = np.copy(A).astype('float64')
    
    for i in range(n):
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            U[j, :] = U[j, :] - factor * U[i, :]
    
    return U

def back_substitution(U):
    n = U.shape[0]
    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        # Only compute dot product for valid elements in the upper triangular part
        if i == n-1:
            x[i] = U[i, -1] / U[i, i]
        else:
            x[i] = (U[i, -1] - np.dot(U[i, i+1:n], x[i+1:n])) / U[i, i]
    
    return x

# Example matrix for Gaussian elimination
A = np.array([[2, 4, -2, 2],
              [4, 9, -3, 8],
              [-2, -1, 7, 10]])

# Perform Gaussian elimination
U = gaussian_elimination(A)
print("Upper triangular matrix after Gaussian elimination: \n", U)

# Perform back substitution to get the solution
x = back_substitution(U)
print("Solution x: ", x)

#I need to check if my solution is correct as well
# Extract the coefficient matrix (first three columns of A) and the constants (last column)
A_coeff = A[:, :-1]  # Coefficients matrix
b = A[:, -1]         # Constants column

# Perform Gaussian elimination and back substitution to get solution
U = gaussian_elimination(A)
x = back_substitution(U)

# Verify by multiplying the coefficient matrix with the solution vector
b_computed = np.dot(A_coeff, x)

# Check if the computed result is close to the original constants
print("Original constants (b): ", b)
print("Computed constants (A * x): ", b_computed)

# Check if they are approximately equal (within a tolerance due to floating-point precision)
if np.allclose(b, b_computed):
    print("The solution is correct.")
else:
    print("The solution is incorrect.")


