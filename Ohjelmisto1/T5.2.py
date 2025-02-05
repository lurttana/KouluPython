luku_lista=[]
for _ in iter(int,1):
    luku=input("anna luku")
    if luku.isnumeric():
        luku_lista.append(int(luku))
    elif luku=="":
        if len(luku_lista)!=0:
            luku_lista.sort(reverse=True)
            print(luku_lista[:5])
        break
