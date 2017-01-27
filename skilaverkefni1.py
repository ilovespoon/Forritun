#24.01.17
#Andri Snær Didriksen Ásmundsson
#Git


#Dæmi 1
print("Velkominn í forritið mit")
print("Dæmi 1")
tala = int(input("Sláðu inn tölu til þess að leggja/margfalda saman "))
tala2 = int(input("Sláðu inn tölu til þess að leggja/Margfalda saman "))
print(tala+tala2)
print(tala*tala2)


#Dæmi 2
print("Dæmi 2")
fornafn = input("Sláðu inn fornafn ")
eftirnafn = input("Sláðu inn Eftirnafn ")
print("Halló", fornafn, eftirnafn)


#Dæmi3
print("Dæmi 3")
hastafir=0
lastafir=0
laghastaf=0

texti=input("Sláðu inn texta : ")
for i in range(len(texti)):
    if texti[i].isupper():
        hastafir=hastafir+1

    if texti[i].islower():
        lastafir=lastafir+1

print(texti)
print("það eru",hastafir,"Hástafir og",lastafir,"lástafir")
