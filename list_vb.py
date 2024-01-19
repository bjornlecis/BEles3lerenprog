steden = ["Berlijn","Rome","Madrid","Parijs"]
steden[0] = "Brussel"
stad = input("geef de naam van de stad")
steden.append(stad)
steden.pop(3) #index
steden.remove("Rome") #waarde
steden.insert(2,"Hasselt")
print(steden)
