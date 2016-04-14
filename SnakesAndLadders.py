from MatrixDefinition import MatrixGenerator
import random
import copy

#Create a SnakesAndLadders Game
#gameMode = 0 means End_mode
#gameMode = 1 means Circle_mode
class SnakesAndLadders:



    def __init__(self,gameMode,trapVector):

        matrixGenerator = MatrixGenerator()

        if(gameMode == 0):
            self.SecurityMatrix = matrixGenerator.defaultSecurityMatrixEnd
            self.RiskyMatrix = matrixGenerator.defaultRiskyMatrixEnd
        else:
            self.SecurityMatrix = matrixGenerator.defaultSecurityMatrixCircle
            self.RiskyMatrix = matrixGenerator.defaultRiskyMatrixCircle

        #We apply the trap vector
        self.applyRetreatToMatrix(trapVector)
        self.applyTrapVectorToMatrix(trapVector)
        self.applyJailToMatrix(trapVector)


        self.costVector = self.buildCostVector()
        print(len(self.costVector))



    def ValueIteration(self):
        utilityVector = [0] * len(self.costVector)
        policyVector = [0] * len(self.costVector)
        for iteration in range(0,100):
            #print("Iteration : "+str(iteration))
            #print("policyVector : " + str(policyVector))
            #print("utilityVector : " + str(utilityVector))
            for item in range(0,len(utilityVector)):
                #print("Item = " + str(item))
                valueWithZero = self.costVector[item]
                for item2 in range(0,len(utilityVector)):
                    #print(self.SecurityMatrix[item][item2]*utilityVector[item2])
                    valueWithZero += self.SecurityMatrix[item][item2]*utilityVector[item2]
                valueWithOne = self.costVector[item]
                for item2 in range(0,len(utilityVector)):
                    valueWithOne += self.RiskyMatrix[item][item2]*utilityVector[item2]
                #print("valueWithZero = "+ str(valueWithZero))
                #print("valueWithOne = "+ str(valueWithOne))
                if valueWithZero < valueWithOne:
                    utilityVector[item] = valueWithZero
                else:
                    utilityVector[item] = valueWithOne

        for item in range(0,len(utilityVector)):
            valueWithZero = 0
            for item2 in range(0,len(utilityVector)):
                valueWithZero += self.SecurityMatrix[item][item2]*(utilityVector[item2] + self.costVector[item])
            valueWithOne = 0
            for item2 in range(0,len(utilityVector)):
                valueWithOne += self.RiskyMatrix[item][item2]*(utilityVector[item2] + self.costVector[item])

            if valueWithOne < valueWithZero:
                policyVector[item] = 1
            else:
                policyVector[item] = 0

        return utilityVector,policyVector


    def policyIteration(self):
        policyVector = [0] * len(self.costVector)
        utilityVector = [0] * len(self.costVector)
        for iteration in range(0,100):
            #print("Iteration : "+str(iteration))
            #print("policyVector : " + str(policyVector))
            #print("utilityVector : " + str(utilityVector))
            for item in range(0,len(utilityVector)):
                #print("Item = " + str(item))
                if policyVector[item] == 0:
                    #use Security matrix
                    sumDesti = 0
                    for item2 in range(0,len(utilityVector)):
                        sumDesti = sumDesti + (self.SecurityMatrix[item][item2]*utilityVector[item2])
                    utilityVector[item] = self.costVector[item] + sumDesti

                else:
                    #use Risky matrix
                    sumDesti = 0
                    for item2 in range(0,len(utilityVector)):
                        sumDesti = sumDesti + (self.RiskyMatrix[item][item2]*utilityVector[item2])
                    utilityVector[item] = self.costVector[item] + sumDesti

                costWithPolicyZero = 0
                for item2 in range(0,len(utilityVector)):
                    costWithPolicyZero = costWithPolicyZero + self.SecurityMatrix[item][item2]*utilityVector[item2]

                costWithPolicyOne = 0
                for item2 in range(0,len(utilityVector)):
                    costWithPolicyOne = costWithPolicyOne + self.RiskyMatrix[item][item2]*utilityVector[item2]

                #print("costWithPolicyZero = "+ str(costWithPolicyZero))
                #print("costWithPolicyOne = "+ str(costWithPolicyOne))
                if costWithPolicyOne < costWithPolicyZero:
                    policyVector[item] = 1
                else:
                    policyVector[item] = 0

        return  utilityVector,policyVector


    #We apply the normal traps to the matrices
    def applyTrapVectorToMatrix(self,trapVector):

        for trapVectorIndex in range(0,len(trapVector)):
            if trapVector[trapVectorIndex] == 1:
                for x in range(0,len(trapVector)):
                    if self.RiskyMatrix[x][trapVectorIndex] >0:
                        temp =  self.RiskyMatrix[x][trapVectorIndex]
                        self.RiskyMatrix[x][0] += temp
                        self.RiskyMatrix[x][trapVectorIndex] = 0


    #We apply the retrat traps to the matrices
    def applyRetreatToMatrix(self,trapVector):
        for trapVectorIndex in range(len(trapVector)-1,-1,-1):
            if trapVector[trapVectorIndex] == 2:
                for x in range(0,len(trapVector)):
                    if self.RiskyMatrix[x][trapVectorIndex] > 0:
                        temp =  self.RiskyMatrix[x][trapVectorIndex]
                        retreatCase = trapVectorIndex -2
                        if retreatCase< 0:
                            self.RiskyMatrix[x][0] += temp
                            self.RiskyMatrix[x][trapVectorIndex] = 0
                        elif trapVectorIndex == 12:
                            self.RiskyMatrix[x][2] += temp
                            self.RiskyMatrix[x][trapVectorIndex] = 0
                        elif trapVectorIndex == 11:
                            self.RiskyMatrix[x][1] += temp
                            self.RiskyMatrix[x][trapVectorIndex] = 0
                        else:
                            self.RiskyMatrix[x][retreatCase] += temp
                            self.RiskyMatrix[x][trapVectorIndex] = 0

    #We apply the jail traps to the matrices
    def applyJailToMatrix(self,trapVector):
        for trapVectorIndex in range(0,len(trapVector)):
            if trapVector[trapVectorIndex] == 3:
                for x in range(0,len(self.RiskyMatrix)):
                    self.RiskyMatrix[x].append(0)
                    self.SecurityMatrix[x].append(0)

                newVectorRisky = copy.copy(self.RiskyMatrix[trapVectorIndex])
                newVectorSecurity = copy.copy(self.SecurityMatrix[trapVectorIndex])
                self.RiskyMatrix.append(newVectorRisky)
                self.SecurityMatrix.append(newVectorSecurity)

                self.RiskyMatrix[trapVectorIndex] = [0] * len(self.RiskyMatrix)
                self.RiskyMatrix[trapVectorIndex][len(self.RiskyMatrix)-1] = 1

    #Build the cost vector depending on the number of states
    #1 everywhere except on the final sqaure (0)
    def buildCostVector(self):
        costVector = list()
        for x in range(0,len(self.RiskyMatrix)):
             costVector.append(1)
        costVector[10] = 0
        return costVector





    #simulate the game with a random function to simulate the dices
    def simulateGame(self,strategy):
        currentPosition = 0
        cost = 0

        while(currentPosition != 10):
            #print("Current position = " + str(currentPosition+1))
            cost += 1
            diceSimulation = random.uniform(0, 1)
            if(strategy[currentPosition] == 0):
                currentPositionDestinationVector = self.SecurityMatrix[currentPosition]
                currentProbability = 0
                possibilityList = list()
                for index in range(0,len(currentPositionDestinationVector)):
                    if currentPositionDestinationVector[index] > 0:
                        currentProbability += currentPositionDestinationVector[index]
                        possibilityList.append((index,currentProbability))

                for position,limit in possibilityList:
                    if diceSimulation <= limit:
                        currentPosition = position
                        break





            else:
                #On utilise la matrix risky
                currentPositionDestinationVector = self.RiskyMatrix[currentPosition]
                currentProbability = 0
                possibilityList = list()
                for index in range(0,len(currentPositionDestinationVector)):
                    if currentPositionDestinationVector[index] > 0:
                        currentProbability += currentPositionDestinationVector[index]
                        possibilityList.append((index,currentProbability))

                for position,limit in possibilityList:
                    if diceSimulation <= limit:
                        currentPosition = position
                        break
        return cost
