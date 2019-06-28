word1 = "pedro"
word2 = "dorep"


def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


def anagram2(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    counter = {}

    for letter in s1:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    for letter in s2:
        if letter in counter:
            counter[letter] -= 1
        else:
            return False

    for k in counter:
        if counter[k] != 0:
            return False

    return True


print(anagram(word1, word2))
print(anagram2(word1, word2))
