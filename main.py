from SnakesAndLadders import SnakesAndLadders

if __name__ == '__main__':

    trapVector = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    trapVector2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    SnakesAndLaddersGame = SnakesAndLadders(0,trapVector2)

    #print(SnakesAndLaddersGame.SecurityMatrix)
    #print(SnakesAndLaddersGame.RiskyMatrix)
    Expec,Dice = SnakesAndLaddersGame.policyIteration()
    print("Cost expectation : " + str(Expec))
    print("Dice choice : " + str(Dice))

    DiceChoiceAlwaysZero = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    DiceChoiceAlwaysOne = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    total = 0

    for x in range(0,1000):
        total += SnakesAndLaddersGame.simulateGame(Dice)
    print("Total cost optimal strategy = " +str(total/1000))

    for x in range(0,1000):
        total += SnakesAndLaddersGame.simulateGame(DiceChoiceAlwaysOne)
    print("Total cost only one = " +str(total/1000))

    for x in range(0,1000):
        total += SnakesAndLaddersGame.simulateGame(DiceChoiceAlwaysZero)
    print("Total cost onle zero= " +str(total/1000))
