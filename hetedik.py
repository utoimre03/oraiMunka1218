import Renszarvas

def beolvas():
    lista = []
    beFile = open("fajlok/Mikulasszan.txt", "r", encoding="UTF-8")
    adatokListaja = beFile.readlines()
    print(adatokListaja)
    for index in range(1, len(adatokListaja), 1):
        if not("Santa Claus" in adatokListaja[index]):
            daraboltSor = adatokListaja[index].split("@")
            # print(daraboltSor)
            szarvas = Renszarvas.Renszarvas(daraboltSor[0], daraboltSor[1], daraboltSor[2], daraboltSor[3])
            # print(szarvas)
            lista.append(szarvas)
            # print(lista)
    beFile.close()
    return lista

def angolMegfelelo(nev: str, lista: list):
    index = 0
    talalat = True
    while index < len(lista) and talalat:
        if lista[index].nevMagyar == nev:
            talalat = False
        index += 1
    if not (talalat):
        print(f"A szarvas angol neve: {lista[index - 1].nevAngol}")
    else:
        print("Nincs ilyen rénszarvas!")

    """
    # érték szerinti bejárás
    for szarvas in szarvasokListaja:
        if szarvas.nevMagyar == "Pompás":
            print(szarvas.nevAngol)
    """

def mikulasSzam(lista: list):
    db = 0
    index = 0
    while index < len(lista):
        daraboltLeiras = lista[index].leiras.split(" ")
        # print(daraboltLeiras)
        index2 = 0
        while index2 < len(daraboltLeiras):
            if daraboltLeiras[index2] == "Mikulás":
                db += 1
            index2 += 1
        index += 1
    print(f"A Mikulás szó előfordulásának száma: {db}")

def atlagMagassag(lista):
    osszeg = 0
    index = 0
    while index < len(lista):
        osszeg += lista[index].magassag
        index += 1
    if len(lista) == 0:
        print("Az átlagmagassága: 0")
    else:
        atlag = osszeg/len(lista)
        print(f"A szarvasok átlagmagassága: {atlag:.2f}")

def parosHelyenRepulokNevei(lista):
    # kiválasztás tétele
    print("A páros helyen repülő szarvasok nevei: ", end="")
    index = 0
    while index < len(lista):
        if lista[index].hely % 2 == 0:
            print(lista[index].nevMagyar+" ", end="")
        index += 1
    print("")

def leghosszabbLeiras(lista):
    maxErtek = len(lista[0].leiras)
    maxIndex = 0
    index = 1
    while index < len(lista):
        if len(lista[index].leiras) > maxErtek:
            maxErtek = len(lista[index].leiras)
            maxIndex = index
        index += 1
    print(f"A leghosszabb leírása {lista[maxIndex].nev} van (hossza: {maxErtek} karakter).")

def hetes():
    # alap feladat
    szarvasokListaja = beolvas()
    # "a" feladat
    for szarvas in szarvasokListaja:
        print(szarvas.kiir())
    # "b" feladat
    print(f"A rénszarvasok száma: {len(szarvasokListaja)}")
    # "c" feladat
    angolMegfelelo("Pompás", szarvasokListaja)
    # "d" feladat
    mikulasSzam(szarvasokListaja)
    # "e" feladat
    atlagMagassag(szarvasokListaja)
    # "f" feladat
    parosHelyenRepulokNevei(szarvasokListaja)
    # "g" feladat
    leghosszabbLeiras(szarvasokListaja)
