def luckyNumbers(matrix: list[list[int]]) -> list[int]:
    list_min = []
    list_max = []
    for r in range(len(matrix)):
        list_min.append(min(matrix[r]))
    for c in range(len(matrix[0])):
        max_val = None
        for r2 in range(len(matrix)):
            if max_val is None or matrix[r2][c] > max_val:
                max_val = matrix[r2][c]
        list_max.append(max_val)
    return list(set(list_min) & set(list_max))


print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(luckyNumbers([[7, 8], [1, 2]]))
