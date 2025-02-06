def gallona_muuntaja(gallonat):
    return gallonat*3.785

while True:
    gallona_syote=input("Anna gallonat:")
    if gallona_syote.isnumeric():
        print(gallona_muuntaja(float(gallona_syote)))
    elif gallona_syote.lstrip("-").isnumeric():
        break
    else:
        print("virheellinen syöte")
