from decimal import *

# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
def zad1(s1,s2):
    a = int(s1[0:2])*1000 + int(s1[3:6])
    b = int(s2[0:2])*1000 + int(s2[3:6])

    for i in range(a,b+1,1):
        result = str(int(i/1000)) + "-" + str(str(i%1000)).zfill(3)
        print(result)


# ZADANIE 2. BRAKUJĄCE ELEMENTY
def zad2(givenList, n):

    baseList = []
    for i in range (1,n+1,1):
        baseList.append(i)

    resultList = []

    for baseElement in baseList:
        if baseElement not in givenList:
            resultList.append(baseElement)

    print(resultList)


# ZADANIE 3. LISTA LICZB
def zad3(a,b,jump):

    listOfNumbers = []
    for i in range (0, int((b-a)/jump+2)):
        listOfNumbers.append(Decimal(a+i*jump))

    print(listOfNumbers)
    #print(type(listOfNumbers[1]))


# WYWOŁANIE FUNKCJI
zad1("79-900", "80-155")
zad2([2,3,7,4,9], 10)
zad3(2,5,0.5)