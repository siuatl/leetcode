def wordPattern(pattern: str, s: str) -> bool:
    s_list = s.split()
    dic_bijec = {}
    seen_str = set()
    if len(s_list) != len(pattern):
        return False
    for let_indx in range(len(pattern)):
        pattern_char = pattern[let_indx]
        word = s_list[let_indx]
        if pattern_char not in dic_bijec:
            if word not in seen_str:
                dic_bijec[pattern_char] = word
                seen_str.add(word)
            else:
                return False
        else:
            if word != dic_bijec[pattern_char]:
                return False
    return True


print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aba", "cat cat cat dog"))
