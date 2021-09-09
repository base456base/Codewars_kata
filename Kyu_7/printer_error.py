#letters from a to m, not a to m is bad. eg. "aaabbbbxzy" --> "3/10"
def printer_error(strings):
    a = [string for string in strings if not (string.lower() >= 'a' and string.lower() <='m')]
    print(f"{len(a)}/{len(strings)}")

printer_error("aaaabbbcccddddxxx")
