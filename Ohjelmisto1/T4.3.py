luvut=[]
while True:
    luku=input("Syötä luku: ")
    if luku=="":
        break
    if luku.isnumeric():
        luvut.append(luku)
if len(luvut)>0:
    print(f"Pienin luku on {min(*luvut)} ja suurin luku on {max(*luvut)}")