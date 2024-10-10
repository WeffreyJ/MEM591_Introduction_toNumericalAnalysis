def back_substitution(U, b):
    n = len(b)
    x = [0] * n  # Initialize solution vector

    for i in range(n - 1, -1, -1):
        sum_val = 0
        for j in range(i + 1, n):
            sum_val += U[i][j] * x[j]
        
        if U[i][i] == 0:
            raise ValueError("Zero on the diagonal. System is not solvable.")
        
        x[i] = (b[i] - sum_val) / U[i][i]

    return x

def forward_substitution(L, b):
    n = len(b)
    x = [0] * n  # Initialize solution vector

    for i in range(n):
        sum_val = 0
        for j in range(i):
            sum_val += L[i][j] * x[j]
        
        if L[i][i] == 0:
            raise ValueError("Zero on the diagonal. System is not solvable.")
        
        x[i] = (b[i] - sum_val) / L[i][i]

    return x

# Test the functions
U = [[2, 5, 5],
     [0, 3, 8],
     [0, 0, 7]]
b_back = [0, 4, 1]

L = [[4, 0, 0],
     [4, 3, 0],
     [5, 3, 7]]
b_forward = [2, 1, 3]

print("Back Substitution Result:")
print(back_substitution(U, b_back))

print("\nForward Substitution Result:")
print(forward_substitution(L, b_forward))
