def scoreOfString(s: str) -> int:
    scor = 0
    for sco in range(1, len(s)):
        scor += abs(ord(s[sco]) - ord(s[sco - 1]))

    return scor


print(scoreOfString(s="hello"))
print(scoreOfString(s="zaz"))
print(scoreOfString(s="leetcode"))
