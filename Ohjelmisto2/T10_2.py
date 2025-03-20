"""Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi."""

from T10_1 import Hissi

class Talo:
    def __init__(self,hissit, alin_kerros, ylin_kerros):
        self.hissit=[]
        for i in range(hissit):
            self.hissit.append(Hissi(alin_kerros,ylin_kerros))
    def aja_hissia(self, hissin_numero, kerros):
        print(f"hissi numero {hissin_numero}")
        self.hissit[hissin_numero-1].siirry_kerrokseen(kerros)