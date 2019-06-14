for n in range(3, 10, 2): # går fra 3-9 med hopp på 2
    print(n)

burgere = ['cheese', 'big mac', 'double cheese', 'chicken salsa']

for n in range(len(burgere)): #lengden på lista
    print(n, burgere[n])


for n in range(len(burgere) -1, -1, -1): # starte på siste, avslutte på første og hopp baklengs
    print(n, burgere[n])