def veel_vouden_7():
    lijst = []
    for i in range(100):
        lijst.append(i*7)
    print(lijst)

def even_oneven_lijst():
    even = []
    oneven = []
    for i in range(10):
        x = int(input("geef een getal in"))
        if x%2==0:
            even.append(x)
        else:
            oneven.append(x)
    print("getallen even",even)
    print("getallen oneven",oneven)

def geef_lijst_met_letters_woord():
    woord = input("geef een woord in")
    letters = []
    for letter in woord:
        letters.append(letter)
    #letters.reverse() keert de lijst om
    return letters
def som_getallen():
    import random
    lijst = []
    for i in range(10):
        lijst.append(random.randint(1,20))
    print(lijst)
    print(sum(lijst))



#veel_vouden_7()
#even_oneven_lijst()
#print(geef_lijst_met_letters_woord())
som_getallen()