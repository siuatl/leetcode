def differenceOfSums(n: int, m: int) -> int:
    sums_2nums = 0
    num_div = 0
    num_not_div = 0
    for u in range(1, n + 1):
        if u % m == 0:
            num_div = num_div + u
        else:
            num_not_div = num_not_div + u
    sums_2nums = num_not_div - num_div

    return sums_2nums


print(differenceOfSums(10, 3))
print(differenceOfSums(5, 6))
print(differenceOfSums(5, 1))
