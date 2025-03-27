"""Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}."""
import mariadb
from flask import Flask, Response
import json

yhteys = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kakka',
         autocommit=True
         )
app = Flask(__name__)
@app.route('/kentta/<icao>')
def icao_haku(icao):
    try:
        sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
        kursori=yhteys.cursor()
        kursori.execute(sql)
        tulos=kursori.fetchall()
        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "ICAO":icao,
            "Name":tulos[0][0],
            "Municipality":tulos[0][1]

        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virhe"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)