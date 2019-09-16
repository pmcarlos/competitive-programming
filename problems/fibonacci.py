def fib(num):
    """Simple fibonacci recursively."""
    if num <= 2:
        return int((num + 1) / 2)
    return fib(num - 1) + fib(num - 2)


print(fib(10))

num = 10
cache = [None] * (num + 1)


def fib_cached(n):
    # if cache[n]:
    #     return cache[n]
    if n <= 2:
        return int((n + 1) / 2)
    else:
        return fib_cached(n - 1) + fib_cached(n - 2)
    # return cache[n]


print("fib cached:", fib_cached(10))


class Memoize:
    """Create a memoization class."""

    def __init__(self, f):
        """Pass a function to the constructor."""
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        """Check wether value is already in memory."""
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


fib_class = Memoize(fib_cached)
print(fib_class(20))


def fibonnaci2(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    return fibonnaci2(n - 1, b, a + b)


def fib_iter(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a
