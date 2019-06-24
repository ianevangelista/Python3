# def hei(navn, tid):
#     print(f'Hei og god {tid} {navn}')

# navn = input('Skriv inn navnet ditt: ')
# tid = input('Skriv inn tid på dagen: ')
# hei(navn, tid)


def areal(radius):
    return(3.142 * radius**2)

def volum(areal, lengde):
    print(areal*lengde)

radius = int(input('Skriv inn radius: '))
lengde = int(input('Skriv inn lengde: '))

areal = areal(radius)
volum(areal, lengde)