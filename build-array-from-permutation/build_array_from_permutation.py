def buildArray(nums: list[int]) -> list[int]:
    nums_array = []
    for i in range(len(nums)):
        nums_array.append(nums[nums[i]])

    return nums_array


print(buildArray([0, 2, 1, 5, 3, 4]))
print(buildArray([5, 0, 1, 2, 3, 4]))
