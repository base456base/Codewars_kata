def no_vowel(string_):
    return "".join(s for s in string_ if s.lower() not in "aeiou")

string_ = "This website is for losers LOL!"
print(no_vowel(string_))
