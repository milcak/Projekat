from knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige
import re

knjige = ucitaj_knjige()
i = 0
z = len(knjige)

duzina = [1, 1, 1, 1, 1, 1, 1, 1, 1]
kljuc = ['sifra', 'naslov', 'isbn', 'autor', 'izdavac', 'broj strana', 'godina', 'cena', 'kategorija']


def duzina_liste2():
    max = '1'
    for i in range(9):
        max = len(str(knjige[0][kljuc[i]]))
        for j in range(z - 1):
            if (max < len(str(knjige[i + 1][kljuc[i]]))):
                max = len(str(knjige[j + 1][kljuc[i]]))
        duzina[i] = max

def prikaz_liste(knjige):
    duzina_liste2()
    print('\nSifra', end="")
    for i in range(duzina[0]+1):
        print(' ', end="")
    print('Naslov', end="")
    for i in range(duzina[1]+1):
        print(' ', end="")
    print('Author', end="")
    for i in range(duzina[2]+1):
        print(' ', end="")
    print('isbn', end="")
    for i in range(duzina[3]+1):
        print(' ', end="")
    print('Izdavac', end="")
    for i in range(duzina[4]+1):
        print(' ', end="")
    print('godina', end="")
    for i in range(duzina[5]+1):
        print(' ', end="")
    print('cena', end="")
    for i in range(duzina[6]+1):
        print(' ', end="")
    print('kategorija', end="")
    for i in range(duzina[7]+1):
        print(' ', end="")
    print('Broj strana', end="\n")
    for knjiga in knjige:
        print(knjiga['Sifra'], end="")
        for i in range(duzina[0]+3-len(str(knjiga['id']))):
            print(' ',end="")
        print(knjiga['naslov'], end="")
        for i in range(duzina[1]+6-len(str(knjiga['naslov']))):
            print(' ',end="")
        print(knjiga['autor'], end="")
        for i in range(duzina[2]+7-len(str(knjiga['autor']))):
            print(' ',end="")
        print(knjiga['isbn'], end="")
        for i in range(duzina[3]+5-len(str(knjiga['isbn']))):
            print(' ',end="")
        print(knjiga['publisher'], end="")
        for i in range(duzina[4]+10-len(str(knjiga['publisher']))):
            print(' ',end="")
        print(knjiga['godina'], end="")
        for i in range(duzina[5]+5-len(str(knjiga['godina']))):
            print(' ',end="")
        print(knjiga['cena'], end="")
        for i in range(duzina[6]+6-len(str(knjiga['cena']))):
            print(' ',end="")
        print(knjiga['kategorija'], end="")
        for i in range(duzina[7]+6-len(str(knjiga['kategorija']))):
            print(' ',end="")
        print(knjiga['broj stranica'], end="\n")
        i+=1


def get_naslov(knjige):
    return knjige.get('title')


def get_kategorija(knjige):
    return knjige.get('kategorija')


def get_autor(knjige):
    return knjige.get('autor')


def get_izdavac(knjige):
    return knjige.get('izdavac')


def get_cena(knjige):
    return knjige.get('cena')


def pretraga_knjiga_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretraga_knjiga_jednakost(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost == knjiga[kljuc]:
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige():
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po kategoriji")
    print("4. Pretraga po autoru")
    print("5. Pretraga po izdavacu")
    print("6. Pretraga po ceni")
    print("0. Napusti pretragu")
    stavka = int(input("Izaberite stavku: "))
    knjige = []
    if stavka == 1:
        sifra = int(input("Unesite sifru: "))
        knjige = pretraga_knjiga_jednakost("sifra", sifra)
    elif stavka == 2:
        naslov = input("Unesite nalsov: ")
        knjige = pretraga_knjiga_string("naslov", naslov)
    elif stavka == 3:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretraga_knjiga_string("kategorija", kategorija)
    elif stavka == 4:
        autor = input("Unesite autora: ")
        knjige = pretraga_knjiga_string("autor", autor)
    elif stavka == 5:
        izdavac = input("Unesite izdavaca: ")
        knjige = pretraga_knjiga_string("autor", izdavac)
    elif stavka == 6:
        cena = input("Unesite cenu: ")
        knjige = pretraga_knjiga_jednakost("autor", cena)
    elif stavka == 0:
        return
    else:
        print("Pogresan unos")

    for knjiga in knjige:
        print(knjiga)


def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp

    return knjige


def sortirane_knjige():
    print("\n1. Sortiraj po sifri")
    print("2. Sortiraj po naslovi")
    print("3. Sortiraj po kategoriji")
    print("4. Sortiraj po autoru")
    print("5. Sortiraj po izdavacu")
    print("6. Sortiraj po ceni")
    print("0. Izlaz")

    stavka = int(input("Izaberite stavku: "))
    knjige = []
    if stavka == 1:
        knjige = sortiraj_knjige("sifra:")

    elif stavka == 2:
        knjige = sortiraj_knjige("naslov:")

    elif stavka == 3:
        knjige = sortiraj_knjige("kategorija:")

    elif stavka == 4:
        knjige = sortiraj_knjige("autor:")

    elif stavka == 5:
        knjige = sortiraj_knjige("izdavac:")

    elif stavka == 6:
        knjige = sortiraj_knjige("cena:")

    elif stavka == 0:
        return
    else:
        print("Pogresan unos!")
    for knjiga in knjige:
        print(knjiga)
