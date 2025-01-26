sp=input("Anna biologinen sukupuoli:")
hb=int(input("Anna hemoglobiini: "))
if sp== "Nainen":
    if hb<117:
        print("Hemoglobiini on alhainen.")
    elif hb>175:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")
elif sp== "Mies":
    if hb<134:
        print("Hemoglobiini on alhainen.")
    elif hb>195:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")