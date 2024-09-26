
def searchpairswithlists(lista,target):
    pairs= []
    for i in range(len(lista)):
        for j in range(i,len(lista)):
            if lista[i]+lista[j]== target:
                if (lista[i],lista[j]) not in pairs:
                    pairs.append((lista[i],lista[j]))
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

