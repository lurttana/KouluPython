import mariadb

yhteys = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kakka',
         autocommit=True
         )
kursori = yhteys.cursor()
sql="SELECT * FROM goal"
kursori.execute(sql)

tulos= kursori.fetchall()
for rivi in tulos:
    print(rivi)