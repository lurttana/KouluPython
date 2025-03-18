"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""
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

autot=[]
for i in range(10):
    autot.append(Auto(f"ABC-{i}",random.randint(100,200)))
kisabool=True
while kisabool:
    for auto in autot:
        auto.kiihdytä(random.randint(-10,15))
        auto.kulje(1)
        if auto.kuljettu_matka>=10000:
            print(auto.rekisteritunnus, auto.kuljettu_matka)
            kisabool=False
