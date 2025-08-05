def twoSum(nums: list[int], target: int) -> list[int]:
    nums_table = dict(zip(nums, range(len(nums))))
    two_nums_lis_i = []
    for i in range(len(nums)):
        subtraction = target - nums[i]
        if subtraction in nums_table:
            if i == nums_table[subtraction]:
                continue
            two_nums_lis_i.append(i)
            two_nums_lis_i.append(nums_table[subtraction])
            break
    return two_nums_lis_i


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
print(twoSum([2, 5, 3, 1, 7], 10))


# def twoSum2(nums: list[int], target: int) -> list[int]:
#     indices_list = []
#     count = 0
#     for i in nums:
#         for n in range(count + 1, len(nums)):
#             sum_nums = i + nums[n]
#             print("mi suma total es:", sum_nums)
#             if sum_nums == target:
#                 indices_list.append(count)
#                 indices_list.append(n)
#         count += 1
#     print(f"la lista es {indices_list}")
