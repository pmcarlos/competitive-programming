def rev_word_1(s):
    return " ".join(reversed(s.split()))


def rev_word_2(s):
    return " ".join(s.split()[::-1])


def rev_word_3(s):
    words = []
    length = len(s)
    spaces = [" "]
    i = length - 1

    while i > 0:
        if s[i] not in spaces:
            word_end = i
            while i > 0 and s[i] not in spaces:
                i -= 1
            words.append(s[i : word_end + 1])
        i -= 1
    return " ".join(words)

rev_word_3("Hi John,   are you ready to go?")

