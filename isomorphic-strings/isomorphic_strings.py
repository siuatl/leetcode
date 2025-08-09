def isIsomorphic(s: str, t: str) -> bool:
    s_to_t = bytearray([128] * 128)
    used = bytearray([False] * 128)
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        char_s = ord(s[i])
        char_t = ord(t[i])
        mapped_value = s_to_t[char_s]
        if mapped_value != 128 and mapped_value != char_t:
            return False
        if used[char_t] and mapped_value == 128:
            return False
        s_to_t[char_s] = char_t
        used[char_t] = True

    return True


print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("foo", "baa"))
print(isIsomorphic("bbbaaaba", "aaabbbba"))
print(isIsomorphic("badc", "baba"))
