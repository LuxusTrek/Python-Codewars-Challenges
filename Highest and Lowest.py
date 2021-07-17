def high_and_low(numbers):
    #Convert the string into a list 
    x = numbers.split()
    c = ""
    for i in range(0, len(x)):
        #convert the str into a int
        x[i] = int(x[i])
    #save the maxa  and min values into and strign with concat
    c = str(max(x)) +" "+str(min(x))
    print(c)
    return c