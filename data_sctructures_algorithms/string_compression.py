def compress(s):
    """Compress using Run Length Encoding (RLE) data compression algorithm."""
    r = ""
    l = len(s)

    if len == 0:
        return ""

    if len == 1:
        return s + "1"

    last = s[0]
    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 0
        i += 1
    r = r + s[i - 1] + str(cnt)

    return r


compressesd = compress("AAAAABBBBCCCC")
print(compressesd)
