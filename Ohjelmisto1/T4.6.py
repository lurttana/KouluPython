import random
amt=int(input("anna määrä:"))
n=0
for i in range(amt):
    x=random.uniform(-1.0,1.0)
    y=random.uniform(-1.0,1.0)
    if x**2+y**2<1:
        n+=1
result=float(4*n/amt)
print(result)

