import mariadb
from geopy.distance import geodesic

yhteys = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kakka',
         autocommit=True
         )

"""Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. 
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. 
Laskenta perustuu tietokannasta haettuihin koordinaatteihin. 
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/. 
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. 
Kirjoita hakukenttään geopy ja vie asennus loppuun."""

def icao_matka_haku():
    icao1=input("Anna ensimmäinen icao koodi: ")
    icao2=input("Anna ensimmäinen icao koodi: ")
    kentat=[]
    sql=f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao1}' OR ident = '{icao2}'"
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos= kursori.fetchall()
    for rivi in tulos:
        kentta=(rivi[0],rivi[1])
        kentat.append(kentta)
    print(f"Kenttien välinen etäisyys on {geodesic(kentat[0], kentat[1]).km:.2f} kilometriä")
icao_matka_haku()