from SnakesAndLadders import SnakesAndLadders

if __name__ == '__main__':

    trapVector = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    trapVector2 = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0]
    trapVector3 = [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1]
    trapVector4 = [0,1,1,1,1,1,1,1,1,1,0,0,0,0,0]

    SnakesAndLaddersGame = SnakesAndLadders(0,trapVector2)
    print("SecurityMatrix")
    for row in range(0,len(SnakesAndLaddersGame.SecurityMatrix)):
        print(str(row) + " " +str(SnakesAndLaddersGame.SecurityMatrix[row]))
    for row in range(0,len(SnakesAndLaddersGame.RiskyMatrix)):
        print(str(row) + " " + str(SnakesAndLaddersGame.RiskyMatrix[row]))

    Expec,Dice = SnakesAndLaddersGame.ValueIteration()
    print("Cost expectation : " + str(Expec))
    print("Dice choice : " + str(Dice))
    '''
    Expec2,Dice2 = SnakesAndLaddersGame.policyIteration()
    print("Cost expectation : " + str(Expec2))
    print("Dice choice : " + str(Dice2))
    '''
    DiceChoiceAlwaysZero = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    DiceChoiceAlwaysOne = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    DiceChoiceAlwaysNew = [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1]

    total = 0
    for x in range(0,10000):
        total += SnakesAndLaddersGame.simulateGame(Dice)
    print("Total cost optimal strategy = " +str(total/10000))

    total = 0
    for x in range(0,10000):
        total += SnakesAndLaddersGame.simulateGame(DiceChoiceAlwaysNew)
    print("Total cost new = " +str(total/10000))

    total = 0
    for x in range(0,10000):
        total += SnakesAndLaddersGame.simulateGame(DiceChoiceAlwaysOne)
    print("Total cost only one = " +str(total/10000))

    total = 0
    for x in range(0,10000):
        total += SnakesAndLaddersGame.simulateGame(DiceChoiceAlwaysZero)
    print("Total cost onle zero= " +str(total/10000))
