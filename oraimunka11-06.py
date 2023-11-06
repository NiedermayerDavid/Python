ev = (int(input("adjon meg egy évszámot: ")))

if ev < 1582:
    print("Nem a gergely-korszakba esik")
else:
    print("A gergely-korszakba esik")

print(ev % 4)
if ev % 4 != 0:
    print("normál év van.")
elif ev % 400 != 0:
    print("normál év van")
elif ev % 100 != 0:
    print("Szökő év van")
else:
    print("szökő év van")