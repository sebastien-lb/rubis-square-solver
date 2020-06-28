from solver import solve_triangular_matrix, get_matrice_square, get_identity, get_tridiagonal

# TEST
# A = get_tridiagonal(3)
# B = get_identity(3)

# solve_triangular_matrix(3, A, B)

# Lvl 1
# A = get_matrice_square(3)
# B = [[1],[0],[2],[1],[0],[2],[1],[0],[2]]

# solve_triangular_matrix(3, A, B)

# Lvl 2
# A = get_matrice_square(3)
# B = [
#     [0],[1],[2],
#     [0],[1],[2],
#     [0],[1],[2],
#     [0],[1],[2]
#     ]

# solve_triangular_matrix(5, A, B)

# Lvl 3
A = get_matrice_square(6)
B = [
    [0],[1],[2],[3],[4],[0],
    [0],[1],[2],[3],[4],[0],
    [0],[1],[2],[3],[4],[0],
    [0],[1],[2],[3],[4],[0],
    [0],[1],[2],[3],[4],[0],
    [0],[1],[2],[3],[4],[0],
    ]

solve_triangular_matrix(5, A, B)

# Test higher
# m = 6
# A = get_matrice_square(m)
# B = get_identity(m*m)
# solve_triangular_matrix(5, A, B)
