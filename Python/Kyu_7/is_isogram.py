# word has no repeating letters (ignore letter case)
def is_isogram(string):
    check = set(string.lower())
    return len(string) == len(check)

print(is_isogram("abcdeA"))
