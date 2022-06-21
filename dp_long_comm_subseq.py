from typing import Any


def lcs(word_a, word_b, len_a, len_b) -> int:
    if len_a == 0 or len_b == 0:
        return 0
    elif word_a[len_a -1] == word_b[len_b -1]:
        return 1 + lcs(word_a, word_b, len_a -1, len_b -1)
    else:
        return max(lcs(word_a, word_b, len_a - 1, len_b), lcs(word_a, word_b, len_a, len_b -1))
        


word_a = "blue"
word_b = "clues"
len_a = len(word_a)
len_b = len(word_b)

print(lcs(word_a, word_b, len_a, len_b))