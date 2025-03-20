"""Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys."""

from T10_1 import Hissi

class Talo:
    def __init__(self,hissit, alin_kerros, ylin_kerros):
        self.hissit=[]
        for i in range(hissit):
            self.hissit.append(Hissi(alin_kerros,ylin_kerros))
    def aja_hissia(self, hissin_numero, kerros):
        print(f"hissi numero {hissin_numero}")
        self.hissit[hissin_numero-1].siirry_kerrokseen(kerros)
    def halytys(self):
        print("alarm")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)

t=Talo(3, 1,5)
for i in range(3):
    t.aja_hissia(i+1,5)
t.halytys()