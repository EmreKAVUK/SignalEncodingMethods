def NZRL(data):
    for i in data:
        if(i == "1"):
            print("_",end = "")
        elif(i=="0"):
            print("¯",end = "")
        else:
            print("Hatali input")
    print("\n")
#–
def NZRI(data):
    isaret = ["_"]
    for i in data:

        if i == "0":
            isaret.append(isaret[-1])

        elif i == "1":
            if isaret[-1] == "_":
                isaret.append("-")

            elif isaret[-1] == "-":
                isaret.append("_")

    for j in isaret:
        print(j,end = "")
    print("\n")

def BipolarAMI(data):
    sayac = 0
    for i in data :
        if(i == "0"):
            print("-",end = "")
        elif(i=="1"):
            # counter tek sayi =   ¯       çift = _
            sayac +=1
            if(sayac % 2 == 0):
                print("_",end = "")
            elif(sayac %2 == 1):
                print("¯",end = "")
    print("\n")

def Pseudoternar(data):
    sayac = 0
    for i in data :
        if(i == "1"):
            print("-",end = "")
        elif(i=="0"):
            # counter tek sayi =   ¯       çift = _
            sayac +=1
            if(sayac % 2 == 0):
                print("_",end = "")
            elif(sayac %2 == 1):
                print("¯",end = "")
    print("\n")



def Manchester(data):
    isaret = []
    for i in data:
        if(i == "0"):
            isaret.append("¯_")
        elif(i=="1"):
            isaret.append("_¯")
    for j in isaret:
        print(j,end = "")
    print("\n")




veri = "01001100011"
Manchester(veri)
Pseudoternar(veri)
BipolarAMI(veri)
NZRI(veri)
NZRL(veri)
