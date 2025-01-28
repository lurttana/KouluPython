import random
arvattava_luku=random.randint(1,10)
while True:
    luku=input("Anna luku: ")
    if luku.isnumeric():
        if int(luku)>arvattava_luku:
            print("Liian suuri arvaus")
        elif int(luku)<arvattava_luku:
            print("Liian pieni arvaus")
        else:
            print("Oikein")
            break
    else:
        print("Virheellinen syöte")