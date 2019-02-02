import time


def pow_fib(n):
    return pow(2 << n, n + 1, (4 << 2 * n) - (2 << n) - 1) % (2 << n)


def for_fib(n):
    a, b = 1, 1
    n = n-2
    for i in range(n):
        a, b = b, a+b
    return b


def list_fib(n):

    list_f = []
    f = 1
    list_f.append(f)
    list_f.append(f)
    for i in range(n-2):
        f = list_f[-1] + list_f[-2]
        list_f.append(f)
    return f


if __name__ == "__main__":
    x = 47
    start = time.time()
    res = list_fib(x)
    elapsed = time.time() - start
    print("Python Computed fib(%s)=%s in %0.8f seconds" % (x, res, elapsed))
