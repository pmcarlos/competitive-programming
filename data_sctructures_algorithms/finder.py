import collections

arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [8, 7, 6, 5, 3, 1]


def finder(arr1, arr2):
    """Find first missing number in arr12."""

    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


result = finder(arr1, arr2)

print(result)


d = collections.defaultdict(int)


def finder2(arr1, arr2):
    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num

    return None


result = finder2(arr1, arr2)

print(result)


def finder3(arr1, arr2):
    result = 0
    print(arr1 + arr2)
    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num
        print(result)

    return result


result = finder3(arr1, arr2)

print(result)
