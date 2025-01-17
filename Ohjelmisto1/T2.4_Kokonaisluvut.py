lista=[]
for i in range(3):
    numbero= int(input("Anna kokonaisluku: "))
    lista.insert(i, numbero)
summa= lista[0] + lista[1] + lista[2]
tulo= lista[0] * lista[1] * lista[2]
keskiarvo= summa / len(lista)
print(f"Summa on: {summa}, tulo on: {tulo} ja keskiarvo {keskiarvo}")
