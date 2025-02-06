lentoasemat={"helsinki-vantaa":"EFHK"}
while True:
    syote=input("mitä tehdään? (haku, uusi, lopetus)")
    if syote=="haku":
        syote=input("anna ICAO koodi")
        for paikat, icaot in lentoasemat.items():
            if syote in icaot:
                print(paikat)
    elif syote=="uusi":
        paikka=input("Anna lentoaseman nimi: ")
        icao=input("Anna ICAO: ")
        lentoasemat[paikka]=icao
    elif syote=="lopetus":
        break