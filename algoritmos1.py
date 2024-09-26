

def searchpairswithlists(lista,target):
    '''
    Usa listas para encontrar los pares de elementos de 
    una lista entera ordenada que sumen target

    Parameters
    ----------
    lista : TYPE
            list
        DESCRIPTION.
        lista ordenada de números enteros
    target : TYPE
            int
        DESCRIPTION.
        Número objetivo 

    Returns
    -------
    pairs : TYPE
            list
        DESCRIPTION.
        pares pertenecientes a la lista que suman dos

    '''
    pairs= []
    for i in range(len(lista)):
        for j in range(i,len(lista)):
            if lista[i]+lista[j]== target:
                if (lista[i],lista[j]) not in pairs:
                    pairs.append((lista[i],lista[j]))
    return pairs


def searchpairswithsets(lista,target):
    '''
    Usa sets para encontrar los pares de elementos de 
    una lista entera ordenada que sumen target


    Parameters
    ----------
    lista : TYPE
            list
        DESCRIPTION.
        lista de números enteros ordenada
    target : TYPE
            int
        DESCRIPTION.
        Número objetivo

    Returns
    -------
    pairs : TYPE
            list
        DESCRIPTION.
        lista de pares de la lista que suman el objetivo

    '''
    pairs= set()
    seen= set()
    for i in range(len(lista)):
        seen.add(lista[i])
        c= target-lista[i]
        if c in seen:
            pairs.add((min(c,lista[i]),max(c,lista[i])))
    return pairs
