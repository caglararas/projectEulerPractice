kare=0
toplam=0
fark=0
toplamkare=0

for i in range(0,101):
     deger=i**2
     kare=kare+deger
print(kare)

for a in range(0,101):
    toplam=toplam+a
toplam = toplam**2


print(toplam)

fark=toplam-kare
print(fark)
---------------------------------------------------------------------------------------------------------------------------------------------------------
10001. ASAL

asalListe = []

for sayi in range(0,200000):
           if sayi > 1:
                for i in range(2, sayi):
                    if (sayi % i) == 0:
                        break
                else:
                    asalListe.append(sayi)
                if len(asalListe)==10001:
                    break


#print(asalListe)
print(asalListe[-1])
print(len(asalListe))

-----------------------------------------------------------------------------------------------------------------------
#13 BASAMAKLI EN BÜYÜK ÇARPIM?
deger=0

buyukSayi ="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

yenitoplam=0


print(len(buyukSayi))
print(buyukSayi[1])
toplam=0
topList=[]
i=0
while i<=987 :
    toplam=int(buyukSayi[i])*int(buyukSayi[i+1])*int(buyukSayi[i+2])*int(buyukSayi[i+3])*int(buyukSayi[i+4])*int(buyukSayi[i+5])*int(buyukSayi[i+6])*int(buyukSayi[i+7])*int(buyukSayi[i+8])*int(buyukSayi[i+9])*int(buyukSayi[i+10])*int(buyukSayi[i+11])*int(buyukSayi[i+12])
    topList.append(toplam)

    i = i + 1

print(max(topList))
-----------------------------------------------------------------------------------------------------------------------

#A+B+C =1000 A2+B2=C2
a,b,c=0,0,0
toplam=0
sonuc=0

for a in range(10,330):
    for b in range(a,500):
        for c in range(b,999):
            if a+b+c==1000:
                    if a**2+b**2==c**2:
                        print("değerler bulundu.")
                        print("a :",a)
                        print("b :",b)
                        print("c :",c)
                        sonuc=a*b*c
                        print(sonuc)

-------------------------------------------------------------------------------


asalListe = []
for sayi in range(2,2000000):
    if sayi > 1:
        for i in range(2, sayi):
            if (sayi % i) == 0:
                break
        else:
            asalListe.append(sayi)

toplam=sum(asalListe)
print(toplam)

toplam=0

toplam=0
for sayi in range(2,2000000):
    if sayi > 1:
        for i in range(2, sayi//2+1):
            if (sayi % i) == 0:
                break
        else:
            print(sayi)
            toplam=toplam+sayi
print("   ",toplam)



#---------------------------------------------------------------------------
from itertools import count

sayiList ="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

duzenliStr= sayiList.replace(" ",'')
myList=sayiList.split()
print(myList)
print(myList[336])
i=0
toplam=0
buyukList=[]
while i<=336:
    toplam=int(myList[i])*int(myList[i+21])*int(myList[i+42])*int(myList[i+63])
    buyukList.append(toplam)

    i=i+1

print(buyukList)
print(len(buyukList))

i=0
toplam2=0
while i<=396:
    toplam2=int(myList[i])*int(myList[i+1])*int(myList[i+2])*int(myList[i+3])
    buyukList.append(toplam2)

    i=i+1

print(len(buyukList))
toplam3=0
i=0
while i<=339:
    toplam3=int(myList[i])*int(myList[i+20])*int(myList[i+40])*int(myList[i+60])
    buyukList.append(toplam3)

    i=i+1
print(len(buyukList))
toplam4=0
i=0
while i<=342:
    toplam4=int(myList[i])*int(myList[i+19])*int(myList[i+38])*int(myList[i+57])
    buyukList.append(toplam4)

    i=i+1

print(len(buyukList))

sonuc=max(buyukList)

print("Sonuç == ",sonuc)



#------------------------------------------------------------------------------------------------
bolenList=[]
i=0

ucgenSayi=[]
j=1
sayi=0

for j in range(1,2000):
        sayi = sayi + j
        j=j+1
        ucgenSayi.append(sayi)

print(ucgenSayi)
print(len(ucgenSayi))
print(ucgenSayi[0])
sonuc=0
bolSayisi = 0
for i in range(0,1999):
        for a in range(1,(ucgenSayi[-1]//2)):
                if a <= ucgenSayi[i]:
                        if ucgenSayi[i] % a == 0 :
                            bolSayisi=bolSayisi+1
                            if bolSayisi>500 :
                                sonuc=ucgenSayi[i]
                            if a == ucgenSayi[i] :
                                bolenList.append(bolSayisi)
                                bolSayisi=0
                                break
                        else:
                            continue
                else:
                    break
print(sonuc)


i=0
j=0
sayi = 0
bolenSayisi =0
sonuc=0
sayiList=[]
asalListe = []
a=0
adet=0
usList=[]
c=0


while bolenSayisi < 500 :
    sayi = sayi + i
    i=i+1
    bolenSayisi=0
    adet=0
    if sayi > 1:
        for a in range(2, sayi):
            if (sayi % a) == 0:
                break
        else:
            asalListe.append(sayi)

    for b in range(0,len(asalListe)):
        if sayi % asalListe[b] == 0:
                adet=adet+1
                usList.append(adet)

    z=len(asalListe)
    for c in range(0,z):
           bolenSayisi=usList[c]+1
           bolenSayisi=bolenSayisi*(usList[c]+1)
print(usList)



def enBuyukAsal(sayi):
    asal = 2
    while asal * asal <= sayi:
        while sayi % asal == 0:
            sayi /= asal
        asal += 1
    if (sayi > 1):
        return sayi
    return asal
print(enBuyukAsal(600851475143))


list = []
for i in range(2,21):
    list.append(i)
for i in range(0, len(list)):
    for j in range(1, i+1):
        if list[i] % list[i-j] == 0:
            list[i] = int(list[i] / list[i-j])
answer = 1
for i in range(0, len(list)):
    answer = answer * list[i]
print(answer)


deger=0
buyukSayi ="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
yenitoplam=0
print(len(buyukSayi))
print(buyukSayi[1])
toplam=0
topList=[]
i=0
while i<=987 :
    toplam=int(buyukSayi[i])*int(buyukSayi[i+1])*int(buyukSayi[i+2])*int(buyukSayi[i+3])*int(buyukSayi[i+4])*int(buyukSayi[i+5])*int(buyukSayi[i+6])*int(buyukSayi[i+7])*int(buyukSayi[i+8])*int(buyukSayi[i+9])*int(buyukSayi[i+10])*int(buyukSayi[i+11])*int(buyukSayi[i+12])
    topList.append(toplam)
    i = i + 1
print(max(topList))


print 'boyunuzu giriniz'

----------------------------------------------------------------------------------------------------------

import math

def kenarAlma():
 kenarlist=[]
 for i in range(3):
    kenardeg = input("kenar giriniz.")
    if(kenardeg =='?'):
        kenardeg = '?'
        kenarlist.append(kenardeg)
    else :
            kenardeg = int(kenardeg)
            kenarlist.append(kenardeg)
 return kenarlist

def kısaKenar(a,c):
   kkenar=(c**2)-(a**2)
   kkenar=math.sqrt(kkenar)
   return kkenar

def hipotenus(a,b):
    ukenar = a**2+b**2
    ukenar = math.sqrt(ukenar)
    return int(ukenar)


kenar1, kenar2, kenar3 = (kenarAlma())

if (kenar1 =='?'):
    print(kısaKenar(kenar2,kenar3))
elif (kenar2=='?'):
    print(kısaKenar(kenar1,kenar3))
else:
    print(hipotenus(kenar1,kenar2))


 def myfunc(n):
     return lambda a : a*n

 mydoubler = myfunc(3)
 print(mydoubler(11))

 carp = lambda b,c : b*c*c
 ca = carp(5,3)
 print(ca)


 ci=[x for x in range(0,101) if x%2==0]

 mapdeneme= list(map(lambda x : x/2 ,ci))
 filterdeneme = list(filter(lambda b: b%3==0,ci))
 print(mapdeneme)
 print(filterdeneme)

 deneme = [sayi*3 for sayi in range(5)]
 print(deneme)

  strlist=['aras' if say%2==0 else 'akdeniz' for say in range[10]]
  print(strlist)

 def generator():
     yield 10
     yield 20
     yield 30

 for value in generator():
     print(value)



 def generator2(a,b,c):
     yield a+b
     yield a+b+c
 for i in generator2(3,3,3):
     print(i)

f=open("deneme.txt","r+")

str=f.read(10)
print(str)
position = f.tell()
print(position)
position = f.seek(7,1)
str=f.read(5)
print(str)













