def permute(s):
    """Given a sing find all possible permutations.

    F.E. Given "abc" results should be ["abc", "acb", "bac", "bca", "cab", "cba"]
    """

    out = []
    if len(s) == 1:
        out = [s]
    for i, let in enumerate(s):
        for perm in permute(s[:i] + s[i + 1 :]):
            out += [let + perm]
    return out


print(permute("abc"))
