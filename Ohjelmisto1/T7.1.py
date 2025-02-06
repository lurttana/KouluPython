vuodenajat= {"kevät":[3,4,5], "kesä":[6,7,8], "syksy":[9,10,11], "talvi":[12,1,2]}
kuukausi=int(input("anna kuukausi (1-12)"))
for vuodenaika, kuukaudet in vuodenajat.items():
    if kuukausi in kuukaudet:
        print(vuodenaika)
