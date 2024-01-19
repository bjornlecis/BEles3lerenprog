def maal_tot_duizend(x):
    teller = 0
    resultaat = 0
    while resultaat < 1000:
        teller += 1
        resultaat = x*teller
        if resultaat < 1000:
            print(resultaat)


def maal_tot_einde(x,eind):
    teller = 0
    resultaat = 0
    while resultaat < eind:
        teller += 1
        resultaat = x * teller
        if resultaat < eind:
            print(resultaat)
def maal_tot_einde_uitbreiding(x,eind):
    teller = 0
    resultaat = 0
    if x>eind:
        wissel = x
        x = eind
        eind = wissel
    while resultaat < eind:
        teller += 1
        resultaat = x * teller
        if resultaat < eind:
            print(resultaat)

def spel_naam(naam):
    for teken in naam:
        print(teken, end = "\t")
def tafelkaart():
    for row in range(1,11):
        for kol in range(1,11):
            print(row*kol, end="\t")
        print()
def tafeldriehoek():
    for row in range(0,11):
        for kol in range(1,row):
            print(row-1*kol, end="\t")
        print()


#maal_tot_duizend(8)
#maal_tot_einde(9,185)
#maal_tot_einde_uitbreiding(200,4)
#spel_naam("Bjorn")
#tafelkaart()
tafeldriehoek()