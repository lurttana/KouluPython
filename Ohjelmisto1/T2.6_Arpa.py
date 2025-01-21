import random
kolmenum=[]
nelinum= []
for i in range(4):
    if i <3:
        kolmenum.append(random.randint(0,9))
    nelinum.append(random.randint(1,6))
print(f"Kolmenumeroinen koodi: {"".join(str(i) for i in kolmenum)}\nNelinumeroinen koodi: {"".join(str(i) for i in nelinum)}")