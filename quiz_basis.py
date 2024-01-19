
import random
def quiz():
    score = 0
    for vraag in range(10):
        x = random.randint(1,10)
        y = random.randint(1,10)
        print("hoeveel is {} x {}".format(x,y))
        antwoord = int(input(""))
        if antwoord == x*y:
            score += 1
    print("uw score is",score)



quiz()