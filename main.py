from SnakesAndLadders import SnakesAndLadders

if __name__ == '__main__':

    #Define here your trap vector
    #0 for safe square
    #1 for normal trap(go back to first square)
    #2 for retrat trap (bock of 2 squares)
    #3 for jail trap(wait a turn becfore playing again)

    trapVector = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    trapVector2 = [3,3,3,3,3,3,3,3,3,3,0,3,3,3,3]
    trapVector3 = [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1]
    trapVector4 = [0,1,1,1,1,1,1,1,1,1,0,0,0,0,0]

    #We create a snakes and ladders game:
    #First arguemnt is the game mode : 0 for end of 11th sqaure mode and 1 for circular mode
    #First arguemtn is the trap vector
    SnakesAndLaddersGame = SnakesAndLadders(0,trapVector2)
    #Uncomment to get the security and risky matrices
    '''
    for row in range(0,len(SnakesAndLaddersGame.SecurityMatrix)):
        print(str(row) + " " +str(SnakesAndLaddersGame.SecurityMatrix[row]))
    for row in range(0,len(SnakesAndLaddersGame.RiskyMatrix)):
        print(str(row) + " " + str(SnakesAndLaddersGame.RiskyMatrix[row]))
    '''
    #We start the value iteration algorithm. After convergence it return the cost expecation of each square and the optimal strategy
    Expec,Dice = SnakesAndLaddersGame.ValueIteration()
    print("Cost expectation : " + str(Expec))
    print("Dice choice : " + str(Dice))
    #We also implemented the policyIteration is an algorithm faster to converge
    '''
    Expec2,Dice2 = SnakesAndLaddersGame.policyIteration()
    print("Cost expectation : " + str(Expec2))
    print("Dice choice : " + str(Dice2))
    '''

    #Here we can define so strategy to compare it to the optimal strategy
    DiceChoiceAlwaysZero = [0] * len(Dice)
    DiceChoiceAlwaysOne = [1] * len(Dice)

    #Here we start the simulation
    total = 0
    for x in range(0,10000):
        total += SnakesAndLaddersGame.simulateGame(Dice)
    print("Total cost optimal strategy = " +str(total/10000))

    total = 0
    for x in range(0,10000):
        total += SnakesAndLaddersGame.simulateGame(DiceChoiceAlwaysOne)
    print("Total cost only one = " +str(total/10000))

    total = 0
    for x in range(0,10000):
        total += SnakesAndLaddersGame.simulateGame(DiceChoiceAlwaysZero)
    print("Total cost onle zero= " +str(total/10000))
