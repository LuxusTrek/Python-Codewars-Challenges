def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    x =[]
    num1=1
    num2=0
    for i in range(a,b+1):
        for j in str(i):
            #print(int(j))
            num2 += pow(int(j),num1)
            num1 +=1
        
        if num2 == i:
            x.append(i)
        num2 = 0
        num1=1

    return x