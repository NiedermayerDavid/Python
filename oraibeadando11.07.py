list=[2,4,6,8,10,16,14,18]
for i in range(len(list)):
    print(list[i])
for i in range(3):
    i = int(input("aj meg egy új lista elemet: "))
    list.append(i)

    print("Lista elemei: ", list)