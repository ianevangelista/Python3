from math import *

""" tall + string
navn = "ian"
alder = 19//1
print("han heter " + navn + " og er " + str(alder) + " ar gammel")
nr = 5**2
print(pow(nr, 2))
print(ceil(3.9))
"""

""" for-loops
for num in (1, 2, 3, 4):
    print(num)
for i in range(5):
    print(i)
"""

"""
navn = input("ditt navn er: ")
alder = input("alder: ")
alder = int(alder)
print("ditt navn er", navn)
print("og du er", alder, "ar gammel")
print(type(navn))
print(type(alder))
"""

"""string
hei = 'hei'
ian = ' ian'
print(hei[0])
print(hei[-3])
print(hei[0:1])
print(hei[-3:2])
print((hei+ian).upper())
ost = "brie, cheddar, stilton"
print(ost.split(','))
print(len(hei))
"""

""" array
fib1 = [1, 1, 2, 3, 5, 8, 13]
print(fib1[0:4])  # skriver ut 0.indeks til 3.
fib2 = [21, 34, 55]
print(fib1+fib2)
fib = fib1+fib2
fib.append(89)  # add
print(fib)
fib.pop()  # sletter siste element
print(fib)
# fib.remove(89)
# del(fib[10])

chars = ['mario', 'luigi', 'bowser']
chars.append(5)
liste = [fib, chars, [1, 2, 3]]
print(liste[1][0])
print(liste)
"""

""" input
radius = input("Skriv inn radius (m):")
areal = pi*int(radius)**2
print("Arealet av sirkelen er:", areal)
"""

""" format: både med og uten
nr1 = 1.95464363462
nr2 = 2.93535362353
print('nr 1 er {0:.4f} og nr2 er {1:.3f}'.format(nr1, nr2))
print(f'nr 1 er {nr1:.4f} og nr2 er {nr2:.3f}')
"""

""" if
alder = int(input("Skriv inn alderen din:"))
if alder < 20:
    print("Du er ung")

elif alder > 50:
    print("Du er gammel")

else:
    print("Skaff deg et liv")


mat = input('Spiser du kjøtt? j/n?: ')
if mat == 'j':
    print("Her er kjøttmenyen")

else:
    print("Her er veggismenyen")
"""
""" for-loops
navn = ['ian', 'juni', 'emir', 'max']
for i in navn:
    if i == 'max':
        print(i)
        break
    else:
        print("hei")
"""
""" while
nr1 = 0
nr2 = 10
while nr1 < nr2:
    if nr1 == 0:
        nr1 += 1
        continue
    if nr1 % 2 == 0:
        print(nr1)
    if nr1 > 8:
        break
    nr1 += 1
"""

""" range
for n in range(0, 20, 5):
    print(n)

biler = ['toyota', 'bmw', 'ferarri', 'lambo', 'mini']
for bil in range(len(biler)):
    print(bil, biler[bil])
"""

"""
def hei(navn, tid):
    print(f'God {tid} {navn}, håper du har det bra!')


navn = input("Skriv inn navn: ")
tid = input("Skriv inn tid på dagen: ")

hei(navn, tid)


def radius(radius):
    print(pi * radius ** 2)


radius(5)
"""
