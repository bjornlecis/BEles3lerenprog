def vul_lijst(aantal):
    lijst_getallen = []
    for i in range(aantal):
        lijst_getallen.append(int(input("geef getal in")))
    return lijst_getallen

def vul_lijst_random(aantal,min,max):
    import random
    lijst_getallen = []
    for getal in range(aantal):
        lijst_getallen.append(random.randint(min,max))
    return lijst_getallen

lijst = (vul_lijst_random(15,1,1500))
print(lijst)
print(min(lijst))