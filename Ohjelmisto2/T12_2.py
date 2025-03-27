"""Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi."""
import json
import requests
def aste_thing():
    api_key="3e4f18a91d34251686319080d0cabb4b"

    paikkakunta=input("Anna paikkakunta: ")
    location_details = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&units=metric&appid={api_key}").json()
    location_details2 = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}").json()
    print(f"{location_details["main"]["temp"]} celsius")
    print(f"{location_details2["main"]["temp"]} kelvin")
aste_thing()