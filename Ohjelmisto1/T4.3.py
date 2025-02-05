luvut=[]
while True:
    luku=input("Syötä luku: ")
    if luku=="":
        break
    if luku.isnumeric():
        luvut.append(luku)
if len(luvut)>0:
    print(f"Pienin luku on {min(*luvut)} ja suurin luku on {max(*luvut)}")

pienin=0
suurin=0
while True:
    luku=input("syötä luku")
    if luku=="":
        break
    if luku.isnumeric():
        if int(luku)<pienin:
            pienin=int(luku)
        elif int(luku)>suurin:
            suurin=int(luku)
print(pienin, suurin)