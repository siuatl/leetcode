def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if left == len(letters):
        return letters[0]
    return letters[left]


print(nextGreatestLetter(["c", "f", "j"], "a"))
print(nextGreatestLetter(["c", "f", "j"], "c"))
print(nextGreatestLetter(["x", "x", "y", "y"], "z"))
