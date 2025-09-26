def MakeisBadVersion(bad_version):
    return lambda version: version >= bad_version


def firstBadVersion(n):
    min_v = 1
    max_v = n
    while min_v < max_v:
        mid = (min_v + max_v) // 2
        if isBadVersion(mid):
            max_v = mid
        else:
            min_v = mid + 1
    return min_v


isBadVersion = MakeisBadVersion(4)
print(firstBadVersion(5))


isBadVersion = MakeisBadVersion(1)
print(firstBadVersion(1))

isBadVersion = MakeisBadVersion(2)
print(firstBadVersion(3))
