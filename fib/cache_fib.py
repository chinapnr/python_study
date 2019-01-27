from fib import cache
import time


@cache.cache(timeout=20, fname="my_cache.pkl")
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    x = 47
    start = time.time()
    res = fib(x)
    elapsed = time.time() - start
    print("Python Computed fib(%s)=%s in %0.8f seconds" % (x, res, elapsed))
