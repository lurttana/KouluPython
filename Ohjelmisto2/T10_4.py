"""Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt."""
import random
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

class Kilpailu:
    def __init__(self, nimi, km, autot):
        self.nimi=nimi
        self.pituus=km
        self.autot=autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        auto_strings=[]
        autos=[]
        for auto in self.autot:
            autos.append([auto.rekisteritunnus, auto.current_speed, auto.kuljettu_matka])
        autos.sort(reverse=True, key=lambda x: x[2])
        for auto in autos:
            auto_strings.append("Auto: {:<7} | nopeus: {:<4}km/h | kuljettu matka: {:<5}km".format(*auto))

        for auto in auto_strings:
            print("-" * len(max(auto_strings, key=len)))
            print(auto)
        print("-"* len(max(auto_strings, key=len)))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka>=self.pituus:
                print("Kisa ohi!")
                k.tulosta_tilanne()
                return True
        return False

autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i + 1}", random.randint(100, 200)))

k= Kilpailu("Suuri Romuralli", 8000,autot)
tunnit=0
while not k.kilpailu_ohi():
    k.tunti_kuluu()
    tunnit+=1
    if tunnit==10:
        print("10 tuntia kulunut")
        k.tulosta_tilanne()
        tunnit=0
