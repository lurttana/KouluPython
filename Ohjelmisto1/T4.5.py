ktunnus="python"
ssana="rules"
false_inputs=0
while false_inputs<5:
    ktunnus_syote=input("Anna käyttäjätunnus: ")
    ssana_syote=input("Anna salasana: ")
    if ssana_syote==ssana and ktunnus_syote == ktunnus:
        print("Tervetuloa")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana")
        false_inputs+=1
        if false_inputs==5:
            print("Pääsy evätty")