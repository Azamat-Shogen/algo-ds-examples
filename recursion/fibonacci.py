
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


# Optimized version using hash table
def fib_optimized(n, hash_t):
    if n == 0 or n == 1:
        return n

    if n in hash_t:
        return hash_t.get(n)

    res = fib_optimized(n-1, hash_t) + fib_optimized(n-2, hash_t)
    hash_t[n] = res
    return res


# print(fib(5))
# print(fib(8))

assert fib_optimized(5, dict()) == 5, 'wrong output'
assert fib_optimized(8, dict()) == 21, 'wrong output'
