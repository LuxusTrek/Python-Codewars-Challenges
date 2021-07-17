def friend(x):
    c=[]
    #make the loop in the list
    for i in x:
        print(i)
        #verify if is alphabetic type
        if i.isalpha():
            if len(i) == 4:
                c.append(i)
    return c