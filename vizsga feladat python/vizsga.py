nev = "a"
elp = 0
maxp = 0

maxp = int(input("Add meg a maximális pontszámot: "))
maxsz = maxp / 100 
maxsz = maxsz * 40
while nev != "":  
    while nev != "":  
        nev = input("Add meg a vizsgázó nevét: ")
        elp = int(input("add meg az elét pontszámot: "))
        break


    def szamol():
        if elp == maxsz or elp > maxsz:
            return(True)
        elif elp < maxsz:
            return(False)


    if szamol() == True:
        print("Sikeres vizsgát tettél!")
    if szamol() == False:
        print("Sikertelen vizsgát tettél.")



