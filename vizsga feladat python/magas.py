import diak
legmagasabb = 0
legnagyobb_diak = ""
file = open("magas.txt", "w")
for i in range(3):
        diak = input("Tanulo neve: ")
        magassag = int(input("Magassaga(cm): "))  
        diaks = [diak, magassag]
        if magassag > legmagasabb:
            legmagasabb = magassag
            legnagyobb_diak = diak
file.write(f'{legnagyobb_diak} a legmagasabb')
file = open("magas.txt", "r")
print(file.read())
