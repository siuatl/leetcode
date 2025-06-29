def luckyNumbers(matrix: list[list[int]]) -> list[int]:
    list_min = [100000] * len(matrix)
    list_max = [0] * len(matrix[0])
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] < list_min[r]:
                list_min[r] = matrix[r][c]
            if matrix[r][c] > list_max[c]:
                list_max[c] = matrix[r][c]

    set_min = set(list_min)
    for v in list_max:
        if v in set_min:
            return [v]
    return []

    # return list(set(list_min) & set(list_max))


print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(luckyNumbers([[7, 8], [1, 2]]))
