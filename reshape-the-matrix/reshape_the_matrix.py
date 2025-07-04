def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    if r * c != len(mat) * len(mat[0]):
        return mat
    new_matrix = []
    for x in range(r):
        new_matrix.append(list(range(c)))
    i = 0
    for r_mat in range(len(mat)):
        for c_mat in range(len(mat[r_mat])):
            new_matrix[int(i/c)][i % c] = mat[r_mat][c_mat]
            i += 1
    return new_matrix


print(matrixReshape([[1, 2], [3, 4]], 1, 4))
# print(matrixReshape([[1, 2, 3], [4, 5, 6]], 1, 6))
# print(matrixReshape([[1, 2, 3], [4, 5, 6]], 2, 3))
print(matrixReshape([[1, 2], [3, 4]], 2, 4))
