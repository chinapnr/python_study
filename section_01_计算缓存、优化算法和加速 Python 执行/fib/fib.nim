

import math, strformat, times

proc fib(n: int): int =
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

when isMainModule:
    let x = 47
    let start = epochTime()
    let res = fib(x)
    let elapsed = (epochtime() - start).round(2)
    stderr.writeLine(&"Nim Computed fib({x})={res} in {elapsed} seconds")