"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km."""

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus= rekisteritunnus
        self.huippunopeus= huippunopeus
        self.current_speed= 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        if nopeuden_muutos<0:
            if self.current_speed+nopeuden_muutos<0:
                self.current_speed=0
            else:
                self.current_speed+=nopeuden_muutos
        if nopeuden_muutos>0:
            if self.current_speed+nopeuden_muutos>self.huippunopeus:
                self.current_speed= self.huippunopeus
            else:
                self.current_speed+=nopeuden_muutos
    def kulje(self, tunnit):
        self.kuljettu_matka+= tunnit*self.current_speed


auto= Auto("ABC-123",142)
auto.kiihdytä(60)
auto.kulje(1.5)
print(f"Auton rekisteritunnus on: {auto.rekisteritunnus}, Huippunopeus: {auto.huippunopeus} km/h, Tämänhetkinen nopeus: {auto.current_speed} km/h, Kuljettu matka: {auto.kuljettu_matka} km")