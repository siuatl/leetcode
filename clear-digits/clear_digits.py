def clearDigits(s: str) -> str:
    for i in s:
        if i.isdigit():
            char_index = s.index(i)
            s = s[:char_index - 1] + s[char_index + 1:]
    return s


print(clearDigits("abc"))
print(clearDigits("cb34"))
print(clearDigits("afts34"))
