"""Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat."""

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

class Sähköauto(Auto):
    def __init__(self,rekisteri,huippunopeus,akkucap):
        super().__init__(rekisteri,huippunopeus)
        self.akkucap=akkucap

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensacap):
        super().__init__(rekisteri,huippunopeus)
        self.bensacap=bensacap

s_auto=Sähköauto("ABC-15", 180, 52.5)
p_auto=Polttomoottoriauto("ACD-123",165,32.3)
s_auto.kiihdytä(60)
p_auto.kiihdytä(60)
s_auto.kulje(3)
p_auto.kulje(3)
print(f"Sähkö: Rek: {s_auto.rekisteritunnus} Speed: {s_auto.current_speed}km/h Matka: {s_auto.kuljettu_matka}km Cap: {s_auto.akkucap} kWh")
print(f"Bensa: Rek: {p_auto.rekisteritunnus} Speed: {p_auto.current_speed}km/h Matka: {p_auto.kuljettu_matka}km Cap: {p_auto.bensacap} l")