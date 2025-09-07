def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    expect_sum = n * (n + 1) // 2
    real_sum = sum(nums)
    return expect_sum - real_sum


print(missingNumber([3, 0, 1]))
print(missingNumber([0, 1]))
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missingNumber([0, 2, 1, 4, 3]))


# def missingNumber2(nums: list[int]) -> int:
#     n = len(nums)
#     if n not in nums:
#         return n
#     for n_index in range(n):
#         if n_index not in nums:
#             return n_index
#     return None
