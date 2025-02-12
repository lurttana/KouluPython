import mariadb

yhteys = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kakka',
         autocommit=True
         )

"""Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja 
tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. 
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, 
että pieniä lentokenttiä on 65 kappaletta, 
helikopterikenttiä on 15 kappaletta jne."""

def kentta_haku():
    ports={"small":0,"medium":0,"large":0,"heli":0,"closed":0}
    maakoodi=input("Anna maakoodi koodi: ")
    sql=f"SELECT type FROM airport WHERE iso_country = '{maakoodi}'"
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos= kursori.fetchall()
    for tyyppi in tulos:
        tyyppi_str= tyyppi[0]
        if tyyppi_str =="small_airport":
                ports["small"]+=1
        elif tyyppi_str == "medium_airport":
                ports["medium"]+=1
        elif tyyppi_str == "large_airport":
                ports["large"]+=1
        elif tyyppi_str=="heliport":
            ports["heli"] += 1
        elif tyyppi_str=="closed":
            ports["closed"] += 1
    for kentta, maara in ports.items():
        if maara>0:
            print(f"{kentta} = {maara}")
kentta_haku()