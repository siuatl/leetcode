def isPerfectSquare(num):
    min_num = 0
    max_num = num
    if num == 1:
        return True
    while min_num < max_num:
        mid = (min_num + max_num) // 2
        mid_squa = mid ** 2
        if mid_squa == num:
            return True
        elif mid_squa > num:
            max_num = mid
        else:
            min_num = mid + 1
    return False


print(isPerfectSquare(16))
print(isPerfectSquare(14))
