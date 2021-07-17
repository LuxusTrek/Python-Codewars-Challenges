def rot13(message):
    print(message)
    half_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    other_half = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    str1 = ""
    for i in message:
        if i.isalpha() == True:
            if i.islower() == True:
                if i in half_alpha:
                    str1 += other_half[half_alpha.index(i)]
                else:
                    str1 += half_alpha[other_half.index(i)]
            else:
                if i.lower() in half_alpha:
                    str1 += other_half[half_alpha.index(i.lower())].upper()
                else:
                    str1 += half_alpha[other_half.index(i.lower())].upper()
        else:
            str1 += i
    return str1