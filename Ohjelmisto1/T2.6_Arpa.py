import random
kolmenum=[]
nelinum= []
for i in range(4):
    if i <3:
        kolmenum.append(random.randint(0,9))
    nelinum.append(random.randint(1,6))
print(*kolmenum)
print(*nelinum)