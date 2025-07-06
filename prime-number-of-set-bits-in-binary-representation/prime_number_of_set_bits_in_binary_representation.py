def countPrimeSetBits(left: int, right: int) -> int:
    set_prime_num = set([2, 3, 5, 7, 11, 13, 17, 19])
    count = 0
    for num in range(left, right + 1):
        bit_count = 0
        while num != 0:
            if num & 1 == 1:
                bit_count += 1
            num >>= 1
        if bit_count in set_prime_num:
            count += 1
    return count


print(countPrimeSetBits(6, 10))
print(countPrimeSetBits(10, 15))
