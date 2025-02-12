import mariadb

yhteys = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kakka',
         autocommit=True
         )

"""Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. 
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. 
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen."""

def icao_haku():
    icao=input("Anna icao koodi: ")
    sql=f"SELECT name FROM airport WHERE ident = '{icao}'"
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos= kursori.fetchall()
    for nimi in tulos:
        print(nimi)

icao_haku()