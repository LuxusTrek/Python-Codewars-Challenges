def create_phone_number(n):
    str1="("
    num = 1
    for i in n:
        if num == 4:
            str1 += ") "
        str1 += ""+str(i)+""
        if num % 3 ==0 and num > 3 and num < 9:
            str1 += "-"
        num += 1
    return str1
    