
m1 = input("Add meg az első mondatot: ")
m2 = input("Add meg a második  mondatot: ")

print("Első mondat: ", "\x1B[3m" + '\033[1m' + m1 + "\x1B[0m")
print("Második mondat: ", "\x1B[3m" + '\033[1m' + m2 + "\x1B[0m")

if len(m1) > len(m2):
    print("Az első mondat hosszabb!")
elif len(m1) < len(m2):
    print ("A második mondat a hosszabb")
else:
    print("A két mondat ugyan olyan hosszú")

