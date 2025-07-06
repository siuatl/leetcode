# Help you to see the bits

# def print_bin_32_bits(num):
#     as_bytes = num.to_bytes(4, 'little', signed=True)
#     as_int = int.from_bytes(as_bytes, 'little', signed=False)
#     print(f"{as_int:032b}")


def findComplement(num: int) -> int:
    num_complement = ~num
    mask = 0
    while num != 0:
        mask <<= 1
        mask |= 1
        num >>= 1
    return num_complement & mask


print(findComplement(5))
print(findComplement(1))
print(findComplement(10))
print(findComplement(4))
