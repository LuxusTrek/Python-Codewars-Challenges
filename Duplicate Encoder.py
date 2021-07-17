from collections import Counter
def duplicate_encode(word):
    count = Counter()
    x = []
    str = ""
    for i in word.lower():
        count[i] += 1
    for n in word.lower():
        if count[n] == 1:
            str +="("
        elif count[n] >= 2:
            str += ")"
    return str