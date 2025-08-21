from collections import Counter
# Faster


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("arma", "masa"))
print(isAnagram("aacc", "ccac"))


# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     count = 0
#     for char in s:
#         if s.count(char) != t.count(char):
#             return False
#         count += 1
#     return True
