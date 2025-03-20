"""Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen."""

class Hissi:
    def __init__(self,alin, ylin):
        self.alin=alin
        self.ylin=ylin
        self.current_kerros=alin
    def siirry_kerrokseen(self, kerros):
        if kerros in range(self.alin, self.ylin):
            self.current_kerros=kerros
    def kerros_ylos(self, amount):
        self.current_kerros+=amount
        return
    def kerros_alas(self,amount):
        self.current_kerros-=amount
        if self.current_kerros<=self.alin:
