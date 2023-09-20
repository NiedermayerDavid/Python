import random

döntetlen = 0
jatekosnyert = 0
gepnyert = 0
gamel = 0

while True:
    játék = "a"
    choice = "ay"

    print("Kő,Papír,Olló")

    print("Válassz a ko,papir,ollo köszül")
    choice = input()

    gch = random.randint(1, 3)

    if gch == 1:
        gch = "ko"
    elif gch == 2:
        gch = "papir"
    elif gch == 3:
        gch = "ollo"

    print(gch)

    if choice == "ko":
        if gch == "ko":
            döntetlen = döntetlen + 1
            print("Döntetlen")
        elif gch == "papir":
            gepnyert = gepnyert + 1
            print("Gép nyert")
        elif gch == "ollo":
            jatekosnyert = jatekosnyert + 1
            print("Te nyertél")

    print(jatekosnyert, gepnyert, döntetlen)

    if choice == "papir":
        if gch == "ko":
            jatekosnyert = jatekosnyert + 1
            print("Te nyertél")
        elif gch == "papir":
            döntetlen = döntetlen + 1
            print("Döntetlen")
        elif gch == "ollo":
            gepnyert = gepnyert + 1
            print("Gép nyert")

    if choice == "ollo":
        if gch == "ollo":
            döntetlen = döntetlen + 1
            print("Döntetlen")

        elif gch == "ko":
            gepnyert = gepnyert + 1
            print("Gép nyert")

        elif gch == "papir":
            jatekosnyert = jatekosnyert + 1
            print("Te nyertél")
    gamel += 1
    # print("\n", gamel)
    if gamel > 5:
        print("szeretnéd folyatni? y,n")
        játék = input()
        if játék == "n":
            break


print("Játékos ennyiszer nyert: ", jatekosnyert)
print("Gép ennyiszer nyert: ", gepnyert)
print("Ennyiszer lett döntetlen: ", döntetlen)
