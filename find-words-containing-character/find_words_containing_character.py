def findWordsContaining(words: list[str], x: str) -> list[int]:
    find_w_index = []
    for i in range(len(words)):
        if x in words[i]:
            find_w_index.append(i)

    return find_w_index


print(findWordsContaining(["leet", "code"], "e"))
print(findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"))
print(findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z"))
