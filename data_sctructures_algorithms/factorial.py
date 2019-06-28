import time

num = 100


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def factorial2(n):
    if n == 1:
        return 1

    subresult = factorial(n - 1)

    return n * subresult


def factorial_acc(n, acc=1):
    if n == 1:
        return acc

    return factorial_acc(n - 1, n * acc)


start = time.time()
print(factorial(num), time.time() - start)

start = time.time()
print(factorial2(num), time.time() - start)

start = time.time()
print(factorial_acc(num), time.time() - start)
