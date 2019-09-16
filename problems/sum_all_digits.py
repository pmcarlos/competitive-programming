def sum_func(n):
    """Sum each digit from a given number F.E. 4321 -> 4+3+2+1=10"""
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_func(n / 10)

