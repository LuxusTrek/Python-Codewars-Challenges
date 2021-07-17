import math
def cakes(recipe, available):
    avaible_cakes = []
    for i in recipe:
        print(i)
        if i in available.keys():
            print(i)
            avaible_cakes.append(math.trunc(available[i]/recipe[i]))
        else:
            return 0
    return min(avaible_cakes)