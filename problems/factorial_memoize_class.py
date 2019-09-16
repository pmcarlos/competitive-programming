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


def factorial(k):
    """Factorial recursive factorial."""
    if k < 2:
        return 1
    return k * factorial(k - 1)


factorial = Memoize(factorial)
print(factorial(4))
