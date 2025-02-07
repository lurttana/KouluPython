def lukusummaaja(luku_lista):
    lukusumma=0
    for i in range(len(luku_lista)):
        lukusumma+=luku_lista[i]
    return lukusumma
    # for luku in lukulista:

kokonaislukuja=[2,3,6,8]
print(lukusummaaja(kokonaislukuja))