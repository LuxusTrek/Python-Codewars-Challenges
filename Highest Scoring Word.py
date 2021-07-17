def high(x):
    puntuacion={}
    num1=0
    alphabet = {
'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10','k' : '11', 'l' : '12', 'm' : '13', 
'n' : '14', 'o' : '15', 'p' : '16','q' : '17', 'r' : '18','s' : '19', 't' : '20', 'u' : '21', 'v' : '22', 
'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}
    for i in x.split():
        #loop throug the list to get the word by word
        for j in i:
            #every iteration loop through the word and make the sum
            num1 += int(alphabet[j])
        puntuacion[i] = num1
        num1 = 0
    print(puntuacion)
    return max(puntuacion,key=puntuacion.get)