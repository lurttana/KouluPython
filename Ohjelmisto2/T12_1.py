"""Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
Käyttäjälle on näytettävä pelkkä vitsin teksti."""
import json
import requests

vastaus = requests.get("https://api.chucknorris.io/jokes/random").json()
print(vastaus["value"])