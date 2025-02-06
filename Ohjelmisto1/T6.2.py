import random
maksimi_tahkot=21
def noppa(tahkot):
    return random.randint(1,tahkot)
noppaluku=0
while noppaluku!=maksimi_tahkot:
    noppaluku=noppa(maksimi_tahkot)
    print(noppaluku)