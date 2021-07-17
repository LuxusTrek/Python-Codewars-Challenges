def digital_root(n):
    #pass to str to be able to iterate
    c = str(n)
    print(n)
    x = 0
    #make the loop 
    for i in c:
        #summ the nums that being iterated 
        x += int(i)
    if x < 10:
        #if the number is less than ten is treturned
        return x
    str2 = str(x)
    v = 0
    for p in str2:
        v += int(p)
        print(v)
    if v < 10:
        return v
    str3 = str(v)
    num3=0
    for p in str3:
        num3 += int(p)
    return num3