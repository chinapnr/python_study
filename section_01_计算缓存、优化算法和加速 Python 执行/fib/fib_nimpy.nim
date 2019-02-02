import nimpy

proc fib(n: int): int {.exportpy.} =
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)