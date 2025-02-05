luku=int(input("anna luku: "))
kertomien_lkm=0
for i in range(luku):
    if luku%(i+1)==0:
        kertomien_lkm+=1
    if kertomien_lkm>2:
        print("luku ei ole alkuluku")
        break
    elif i+1==luku:
        print("luku on alkuluku")
