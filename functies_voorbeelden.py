from colorama import Fore
"""def dubbel(x):
    print(x*2)

def lees_en_print_dubbel_getal():
    getal = int(input("geef een getal in"))
    print("het dubbel van het getal is",getal*2)

for i in range(1,11):
    lees_en_print_dubbel_getal()"""

"""def zeg_hallo(naam):
    boodschap = "hallo {}".format(naam)
    return (boodschap)

begroeting = zeg_hallo("Iedereen")
print(begroeting)
"""
def zeg_in_groene_hoofdletter(tekst):
    tekst = tekst.upper()
    print(Fore.GREEN+tekst+Fore.RESET)

zeg_in_groene_hoofdletter("Dit is een tekst")
print("hallo")
