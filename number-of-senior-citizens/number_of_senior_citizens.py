def countSeniors(details: list[str]) -> int:
    count = 0
    for s in details:
        if int(s[11:13]) > 60:
            count += 1
    return count


print(countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
print(countSeniors(["1313579440F2036", "2921522980M5644"]))
print(countSeniors(["4536789201M0532"]))
