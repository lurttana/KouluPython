def lukusuodatin(luku_lista):
    for luku in luku_lista:
        if luku%2!=0:
            luku_lista.remove(luku)
    return luku_lista

kokonaislukuja=[2,3,6,8]
print(kokonaislukuja)
print(lukusuodatin(kokonaislukuja))