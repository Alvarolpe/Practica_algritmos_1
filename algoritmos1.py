
def searchpairswithlists(lista,target):
    pairs= []
    for i in range(len(lista)):
        for j in range(len(lista)-i):
            if lista[i]+lista[j+i]== target:
                if (lista[i],lista[j+i]) not in pairs:
                    pairs.append((lista[i],lista[j+i]))
    return pairs



def searchpairswithsets(lista,target):
    pairs= set()
    seen= set()
    for i in range(len(lista)):
        seen.add(lista[i])
        c= target-lista[i]
        if c in seen:
            pairs.add((min(c,lista[i]),max(c,lista[i])))
    return pairs

