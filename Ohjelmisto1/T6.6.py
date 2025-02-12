import math
def pizza_laskuri(halkaisija, hinta):
    halkaisija=halkaisija*0.01
    pinta_ala=math.pi*halkaisija
    return hinta/pinta_ala

pizza_list=[]
pizza_lkm=0
while pizza_lkm<2:
    pizza_halk = input(f"anna pizzan {pizza_lkm+1} halk: ")
    pizza_hint = input(f"anna pizzan {pizza_lkm+1} hinta: ")
    if pizza_halk.isnumeric() and pizza_hint.isnumeric():
        pizza_list.append(pizza_laskuri(float(pizza_halk), float(pizza_hint)))
        pizza_lkm+=1
    else:
        print("virheellinen syöte")
halvempi_pizza=min(pizza_list)
halvempi_pizza_index=pizza_list.index(halvempi_pizza)
print(f"pizza {halvempi_pizza_index+1} on halvempi.")