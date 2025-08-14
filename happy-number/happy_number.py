def isHappy(n: int) -> bool:
    if n == 1:
        return True
    nums_seen = set()
    while n != 1 and n not in nums_seen:
        nums_seen.add(n)
        n = sum(int(str_num) ** 2 for str_num in str(n))
    if n != 1:
        return False
    return True


print(isHappy(19))
print(isHappy(2))
print(isHappy(7))
