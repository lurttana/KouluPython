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
        if kerros<self.alin:
            kerros=self.alin
        elif kerros>self.ylin:
            kerros=self.ylin
        if kerros==self.current_kerros:
            print(f"hissi on jo kerroksessa {self.current_kerros}")
        else:
            print(f"hissi lähtee kerroksesta {self.current_kerros}")
        while self.current_kerros!=kerros:
            if self.current_kerros>kerros:
                self.kerros_alas()
            elif self.current_kerros<kerros:
                self.kerros_ylos()

    def kerros_ylos(self):
        self.current_kerros+=1
        print(self.current_kerros)

    def kerros_alas(self):
        self.current_kerros-=1
        print(self.current_kerros)