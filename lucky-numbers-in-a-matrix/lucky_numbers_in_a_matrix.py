def luckyNumbers(matrix: list[list[int]]) -> list[int]:
    lucky_number = []
    for r in range(len(matrix)):
        pos_min = None
        for c in range(len(matrix[r])):
            if pos_min is None or matrix[r][c] < matrix[r][pos_min]:
                pos_min = c

        pos_max = None
        for f in range(len(matrix)):
            if pos_max is None or matrix[f][pos_min] > matrix[pos_max][pos_min]:
                pos_max = f
        if r == pos_max:
            lucky_number.append(matrix[pos_max][pos_min])
            break

    return lucky_number


print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(luckyNumbers([[7, 8], [1, 2]]))
