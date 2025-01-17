leiviska=float(input("Montako leiviskää?: "))
naula=float(input("Montako naulaa?: "))
luoti=float(input("Montako luotia?: "))
total=(leiviska*20*32)+(naula*32)+luoti
massa=total*13.3
print(f"{int(massa/1000)} kilogrammaa ja {round(massa%1000, 2)} grammaa")
