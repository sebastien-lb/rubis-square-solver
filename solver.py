import math

def display_matrice(A):
    for l in A:
        print(l)

def get_identity(n):
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        A[i][i] = 1
    return A

def get_tridiagonal(n):
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        A[i][i] = 1
        A[i][min(i+1, n-1)] = 1
        A[i][max(i-1, 0)] = 1
    return A


def get_matrice_square(square_side_length):
    n = square_side_length**2
    A = [[0 for i in range(n)] for j in range(n)] 
    for i in range(n):
        A[i][i] = 1
        if (i+1) % square_side_length != 0:
            A[i][min(i+1, n-1)] = 1
        if i % square_side_length != 0:
            A[i][max(i-1, 0)] = 1

        if i + square_side_length < n:
            A[i][i+square_side_length] = 1
        if i - square_side_length >= 0:
            A[i][i - square_side_length] = 1
    
    return A

# display_matrice(get_matrice_square(2))
# display_matrice(get_matrice_square(3))
assert get_matrice_square(2) == [[1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1]]

def switch_line(A,i,j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    return A

assert switch_line([[1,2,0],[1,3,1],[4,1,1]], 1, 2) == [[1,2,0],[4,1,1],[1,3,1]]

""" 
    Multiply the line i of the matrice A by x in Z/nZ
"""
def mult_line(n, A, i, x):
    l = [x*A[i][j] % n for j in range(len(A[0]))]
    A[i] = l
    return A

"""
    Eliminate A[j][i] in Z/nZ using A[i][i] with A[i][i] == 1
    A[j] - A[i]*f
"""
def eliminate_factor_i_in_line_j(n, A, i, j, f):
    l = [((A[j][p] - A[i][p]*f) % n) for p in range(len(A[0]))]
    A[j] = l
    return A

assert eliminate_factor_i_in_line_j(3,[[1,1,1],[0,1,2],[0,1,1]], 1, 2, 1) == [[1,1,1],[0,1,2],[0,0,2]]

def get_inverse_for_7(v):
    if v == 0:
        raise Exception("0 does not have an invers")
    elif v == 1:
        return 1
    elif v == 2:
        return 4
    elif v == 3:
        return 5
    elif v == 4:
        return 2
    elif v == 5:
        return 3
    else:
        return 6

def get_inverse_for_5(v):
    if v == 0:
        raise Exception("0 does not have an invers")
    elif v == 1:
        return 1
    elif v == 2:
        return 3
    elif v == 3:
        return 2
    else:
        return 4

def get_inverse_for_3(v):
    if v == 0:
        raise Exception("0 does not have an invers")
    elif v == 1:
        return 1
    else:
        return 2


""" 
Solving the equation AX - B = 0
"""
def pivot_gauss_p_colors(p, A, B):
    print("Starting Gauss pivot")
    display_matrice(A)
    display_matrice(B)
    inverse_function = lambda x: x
    if p == 3:
        inverse_function = get_inverse_for_3
    elif p == 5:
        inverse_function = get_inverse_for_5
    elif p == 7:
        inverse_function = get_inverse_for_7
    n = len(A)
    for i in range(n):
        found = False
        for j in range(i, n):
            if A[j][i] == 0:
                continue
            else:
                found = True
                # print("Line " + str(j) + " will be used as pivot")
                A = switch_line(A, i, j)
                B = switch_line(B, i, j)
                d = A[i][i]
                inv_d = inverse_function(d)
                A = mult_line(p, A, i, inv_d)
                B = mult_line(p, B, i, inv_d)
                break
        if not found:
            display_matrice(A)
            raise Exception("No pivot found for line " + str(i))
        # Line i is ok with a pivot. Pivot value at 1
        # eliminating all coeff in lines above
        # print("Starting reduction")
        for u in range(min(i+1,n), n):

            if A[u][i] != 0:
                # print("Eliminating line " + str(u) + " with line " + str(i))
                factor = A[u][i]
                A = eliminate_factor_i_in_line_j(p, A, i, u, factor)
                # display_matrice(A)
                B = eliminate_factor_i_in_line_j(p, B, i, u, factor)
                # display_matrice(B)
        # print("Reduction done, here is the matrix")
        # display_matrice(A)
        # display_matrice(B)    
    print("done")
    display_matrice(A)
    display_matrice(B)
    return A, B

    
"""
Solve the system anr return thee solution
"""
def solve_triangular_matrix(p, A, B):
    A, B = pivot_gauss_p_colors(p, A, B)
    n = len(A)
    # Remonté de la matrice
    for i in range(n):
        for j in range(min(i+1,n), n):
            factor = A[n-j-1][n-i-1]
            A[n-j-1] = [(A[n-j-1][u] - factor*A[n-i-1][u]) % p for u in range(len(A[0]))]
            B[n-j-1] = [(B[n-j-1][u] - factor*B[n-i-1][u]) % p for u in range(len(B[0]))]
    
    print("Solving done")
    display_matrice(A)
    display_matrice(B)
    print_B_matrix_as_square(B)


"""
    Take a vector matrix B and display it as a square
"""
def print_B_matrix_as_square(B):
    n = len(B)
    l = int(math.sqrt(n))
    b = [ [] for i in range(l)]
    for i in range(l):
        b[i] = [B[l*i + j][0] for j in range(l)]
        
    display_matrice(b)

