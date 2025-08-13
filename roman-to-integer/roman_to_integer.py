def romanToInt(s: str) -> int:

    romanToInt_dic = [0] * 128
    romanToInt_dic[ord('I')] = 1
    romanToInt_dic[ord('V')] = 5
    romanToInt_dic[ord('X')] = 10
    romanToInt_dic[ord('L')] = 50
    romanToInt_dic[ord('C')] = 100
    romanToInt_dic[ord('D')] = 500
    romanToInt_dic[ord('M')] = 1000

    conca_rom_nums = [(ord('I'), ord('V')),
                      (ord('I'), ord('X')),
                      (ord('X'), ord('L')),
                      (ord('X'), ord('C')),
                      (ord('C'), ord('D')),
                      (ord('C'), ord('M')),
                      ]

    total = 0
    for i in range(len(s)):
        int_val = romanToInt_dic[ord(s[i])]
        if i+1 < len(s) and (ord(s[i]), ord(s[i+1])) in conca_rom_nums:
            total -= int_val
        else:
            total += int_val

    return total


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("MMCMXII"))


# def romanToInt(self, s: str) -> int:
#     romanToInt_dic = {'I': 1, 'V': 5, 'X': 10,
#                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     conca_rom_nums = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
#     total = 0
#     for i in range(len(s)):
#         int_val = romanToInt_dic.get(s[i])
#         # total += int_val
#         if i+1 < len(s) and s[i] + s[i + 1] in conca_rom_nums:
#              total -= int_val
#         else:
#             total += int_val
#     return total
