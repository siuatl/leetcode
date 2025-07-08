# Help you to see the bits

# def print_bin_32_bits(num):
#     as_bytes = num.to_bytes(4, 'little', signed=True)
#     as_int = int.from_bytes(as_bytes, 'little', signed=False)
#     print(f"{as_int:032b}")


# First opcion (more simple)
def hasAlternatingBits(n: int) -> bool:
    pre_bit = n & 1
    while n != 0:
        n >>= 1
        if pre_bit == n & 1:
            return False
        pre_bit = n & 1
    return True


print(hasAlternatingBits(5))
print(hasAlternatingBits(7))
print(hasAlternatingBits(11))
print(hasAlternatingBits(9))
print(hasAlternatingBits(4))


# Second option to use


def hasAlternatingBits_2(n: int) -> bool:
    first_bit = n & 1
    num = n
    n >>= 1
    second_bit = n & 1
    if first_bit == second_bit:
        return False

    x = -(~(num ^ n))
    if x.bit_count() == 1 and x > num:
        return True
    return False
