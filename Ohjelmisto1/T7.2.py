nimi=input("anna nimi")
nimet=set()
while nimi!= "":
    if nimi not in nimet:
        nimet.add(nimi)
        print("uusi nimi")
    else:
        print("aiemmin syötetty nimi")
    nimi = input("anna nimi")
print(*nimet)