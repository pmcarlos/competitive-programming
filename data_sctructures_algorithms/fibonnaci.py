def fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib1 = fibonnaci(n - 1)
    fib2 = fibonnaci(n - 2)
    return fib1 + fib2


def fibonnaci2(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    return fibonnaci2(n - 1, b, a + b)


print(fibonnaci(10))
print(fibonnaci2(10))
