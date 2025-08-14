def containsDuplicate(nums: list[int]) -> bool:
    dic_cont = {}
    for n in nums:
        dic_cont[n] = dic_cont.get(n, 0) + 1
        if dic_cont[n] > 1:
            return True
    return False


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
