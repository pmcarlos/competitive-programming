def uniq_char(s):
    return len(set(s)) == len(s)


def uniq_char_2(s):
    chars = set()

    for c in s:
        if c in chars:
            return False
        else:
            chars.add(c)
    return True


s = "abcde"
print(uniq_char(s))
s = "abbcd"
print(uniq_char(s))
s = "abcde"
print(uniq_char_2(s))
s = "abbcd"
print(uniq_char_2(s))
