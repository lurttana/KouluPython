"""Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää."""

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


auto= Auto("ABC-123",142)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(auto.current_speed)
auto.kiihdytä(-200)
print(auto.current_speed)
print(f"Auton rekisteritunnus on: {auto.rekisteritunnus}, Huippunopeus: {auto.huippunopeus} km/h, Tämänhetkinen nopeus: {auto.current_speed} km/h, Kuljettu matka: {auto.kuljettu_matka}")