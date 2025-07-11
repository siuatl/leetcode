import itertools


def addBinary(a: str, b: str) -> str:
    # option_1

    max_len = max(len(a), len(b)) + 1
    sum_list = list("0" * max_len)
    carry_num = 0
    sum_index = max_len - 1
    for digit_a, digit_b in itertools.zip_longest(reversed(a), reversed(b), fillvalue="0"):
        bits_add = (ord(digit_a) & 1) + \
            (ord(digit_b) & 1) + carry_num
        carry_num = 0

        if bits_add == 3:
            sum_list[sum_index] = "1"
            carry_num = 1
        elif bits_add == 2:
            carry_num = 1
        elif bits_add == 1:
            sum_list[sum_index] = "1"
        sum_index -= 1

    if carry_num == 1:
        sum_list[0] = "1"
        return "".join(sum_list)

    return "".join(sum_list[1:])


print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
print(addBinary("1111", "11"))
print(addBinary("0", "0"))
print(addBinary("1111", "1111"))


def addBinary2(a: str, b: str) -> str:
    # option_2
    bits_add = bin(int(a, 2) + int(b, 2))
    return str(bits_add[2:])


def addBinary3(a: str, b: str) -> str:
    # option_3
    sum_str = ""
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(max(len(a), len(b)))
    carry_num = 0
    for char_index in range(len(a)-1, -1, -1):
        bits_add = (ord(a[char_index]) & 1) + \
            (ord(b[char_index]) & 1) + carry_num
        carry_num = 0
        if bits_add == 0:
            sum_str += "0"
        elif bits_add == 3:
            sum_str += "1"
            carry_num = 1
        elif bits_add == 2:
            sum_str += "0"
            carry_num = 1
        elif bits_add == 1:
            sum_str += "1"

    if carry_num == 1:
        sum_str += "1"

    return sum_str[::-1]


def addBinary4(a: str, b: str) -> str:
    # option_4
    sum_str = ""
    carry_num = 0
    for digit_a, digit_b in itertools.zip_longest(reversed(a), reversed(b), fillvalue="0"):
        bits_add = (ord(digit_a) & 1) + \
            (ord(digit_b) & 1) + carry_num
        carry_num = 0
        if bits_add == 0:
            sum_str += "0"
        elif bits_add == 3:
            sum_str += "1"
            carry_num = 1
        elif bits_add == 2:
            sum_str += "0"
            carry_num = 1
        elif bits_add == 1:
            sum_str += "1"

    if carry_num == 1:
        sum_str += "1"

    return sum_str[::-1]
