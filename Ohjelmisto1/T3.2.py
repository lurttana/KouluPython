luokka= input("Anna hyttiluokka (LUX,A,B,C):")
if luokka == "LUX":
    print(f"{luokka} on parvekkeellinen hytti yläkannella.")
elif luokka =="A":
    print(f"{luokka} on ikkunallinen hytti autokannen yläpuolella.")
elif luokka =="B" or luokka=="C":
    print(f"{luokka} on ikkunaton hytti autokannen alapuolella.")
else:
    print(f"{luokka} ei ole hyttiluokka")