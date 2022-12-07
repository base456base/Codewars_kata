"""
Implement a pseudo-encryption algorithm which given a string S and an integer N 
concatenates all the odd-indexed characters of S with all the even-indexed characters of S, 
this process should be repeated N times.

Examples:

    encrypt("012345", 1)  =>  "135024"
    encrypt("012345", 2)  =>  "135024"  ->  "304152"
    encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

    encrypt("01234", 1)  =>  "13024"
    encrypt("01234", 2)  =>  "13024"  ->  "32104"
    encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"

Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without change
"""

from typing import OrderedDict


def decrypt(encrypted_text, n):
    if n < 1:
        return encrypted_text
    m=1
    while True:
        if encrypted_text == encrypt(encrypted_text, m):
            while True:
                if m > n:
                    break
                m += m
            break
        m += 1
    return encrypt(encrypted_text, m-n)

def encrypt(text, n):
    if n < 1:
        return text
    even = "".join([char for idx, char in enumerate(text) if idx%2 == 0])
    odd = "".join([char for idx, char in enumerate(text) if idx%2 == 1])
    result = odd + even
    if n > 1:
        return encrypt(result, n-1)
    return result

print(decrypt(" Tah itse sits!", 3))

"""
the best

def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text



def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
"""