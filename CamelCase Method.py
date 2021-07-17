def camel_case(string):
    x= string.split()
    str1=""
    for i in x:
        str1 += i.capitalize()
    return str1.replace(" ","")
    