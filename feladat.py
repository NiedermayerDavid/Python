import math
x = 0
r = 0
x = int(input(print("Adja meg a kör átmérőjét \b")))
r = x / 2
T = r*r * math.pi
K = 2*r *math.pi
print("A kör Területe:")
print("{:.2f}".format(T))
print("A kör Kerülete:")
print("{:.2f}".format(K))

kmh = 0
mi = 0
kmh = int(input(print("Adja meg a km/h-át")))
mi = kmh * 0.6213711922375
print("Átváltva Mérföld/órába:")
print("{:.2f}".format(mi))

mp = 0
time = 0
timemar = 0

mp = int(input(print("Adja meg az eltelt időt mp-ben")))
time = mp // 60
timemar = mp % 60

print("A megadott idő percben és másodpercben:")
print(time, "perc", timemar, "mp")
