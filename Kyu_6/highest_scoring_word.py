"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""

def high(x):
    words = x.split()
    scores = []
    for word in words:
        score = [ord(char) - ord('a') + 1 for char in word]
        scores.append(sum(score))
    print(scores)
    return words[scores.index(max(scores))]

print(high('what time are we climbing up the volcano'))

"""
the best
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
"""