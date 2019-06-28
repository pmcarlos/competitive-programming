def pair_sum(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        diff = k - num
        if diff not in seen:
            seen.add(num)
        else:
            output.add((num, diff))

    return output


result = pair_sum([1, 3, 2, 4, 5, 6, 0], 4)
print(result)

