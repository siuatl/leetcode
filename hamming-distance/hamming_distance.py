def hammingDistance(x: int, y: int) -> int:
    # with one line :)
    # return (x ^ y).bit_count()
    x_xor_y = x ^ y
    count = 0
    while x_xor_y != 0:
        if x_xor_y & 1 == 1:
            count += 1
        x_xor_y >>= 1
    return count


print(hammingDistance(1, 4))
print(hammingDistance(3, 1))
