import string

def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    for i in alphabet:
        if i not in s.lower():
            return False
    return True
    