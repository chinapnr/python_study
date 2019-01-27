import time


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def cache_fib(n, _cache={}):

    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, cache_fib(n-1) + cache_fib(n-2))
    return n


def pow_fib(n):
    return pow(2 << n, n + 1, (4 << 2 * n) - (2 << n) - 1) % (2 << n)


def ab_fib(n):
    a, b = 1, 1
    n = n-2
    for i in range(n):
        a, b = b, a+b
    return b


if __name__ == "__main__":
    x = 47
    start = time.time()
    res = cache_fib(x)
    elapsed = time.time() - start
    print("Python Computed fib(%s)=%s in %0.8f seconds" % (x, res, elapsed))
