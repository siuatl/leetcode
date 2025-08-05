def majorityElement(nums: list[int]) -> int:
    count = 0
    element = 0
    for n in nums:
        if count == 0:
            element = n
        if n == element:
            count += 1
        else:
            count -= 1
    return element


print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))


# def majorityElement(nums: list[int]) -> int:
#     freq = {}
#     majority_freq = int(len(nums) / 2) + 1
#     for n in nums:
#         new_freq = freq.get(n, 0) + 1
#         if new_freq == majority_freq:
#             return n
#         freq[n] = new_freq

#     return None
