def intersection(nums1, nums2):
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)

    ls_intersection = []
    for num in set_nums2:
        if num in set_nums1:
            ls_intersection.append(num)
    return ls_intersection


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
