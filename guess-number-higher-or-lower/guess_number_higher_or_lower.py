def guess(num):
    if num > guess.pick:
        return -1
    elif num < guess.pick:
        return 1
    else:
        return 0


def guessNumber(n):
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        match guess(mid):
            case 1:
                left = mid + 1
            case -1:
                right = mid - 1
            case _:
                return mid

    return left


guess.pick = 6
print(guessNumber(10))
