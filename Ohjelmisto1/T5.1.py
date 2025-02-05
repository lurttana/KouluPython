import random
lukumaara=int(input("Montako noppaa: "))
summa=0
for i in range(lukumaara):
    luku=random.randint(1,6)
    summa+=luku
print(summa)
