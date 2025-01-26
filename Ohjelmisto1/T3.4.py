vuosi=int(input("Anna vuosiluku:"))
if vuosi%100==0:
    if vuosi%400==0:
        print(f"Vuosi {vuosi} on karkausvuosi")
    else:
        print(f"Vuosi {vuosi} ei ole karkausvuosi")
elif vuosi %4==0:
    print(f"Vuosi {vuosi} on karkausvuosi")
else:
    print(f"Vuosi {vuosi} ei ole karkausvuosi")

