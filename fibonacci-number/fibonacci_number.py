def fib(n: int) -> int:
    if n in fib.cache:
        return fib.cache[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib.cache[n] = fib(n - 1) + fib(n - 2)
    return fib.cache[n]


fib.cache = {}


print(fib(2))
print(fib(3))
print(fib(4))
print(fib(7))
