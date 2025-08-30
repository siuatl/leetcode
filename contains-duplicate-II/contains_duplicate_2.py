def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    dict_indx = {}
    for i in range(len(nums)):
        if nums[i] in dict_indx:
            if abs(i - dict_indx[nums[i]]) <= k:
                return True
        dict_indx[nums[i]] = i
    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))
print(containsNearbyDuplicate([1, 0, 1, 1], 1))
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
