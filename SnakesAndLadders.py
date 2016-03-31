from MatrixDefinition import MatrixGenerator
import random
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

        self.applyTrapVectorToMatrix(trapVector)
        #self.applyRetreatToMatrix(trapVector,gameMode)

        #self.costVector = [100,90,80,70,60,50,40,30,20,10,0,40,30,20,10]
        #self.costVector = [10,9,8,7,6,5,4,3,2,1,0,4,3,2,1]
        self.costVector = [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1]
        #self.costVector = self.buildCostVector(trapVector)


    def ValueIteration(self):
        utilityVector = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        policyVector = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
        policyVector = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
        utilityVector = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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

    def buildCostVector(self,trapVector):
        costVector = [10,9,8,7,6,5,4,3,2,1,0,4,3,2,1]
        for trapVectorIndex in range(0,len(trapVector)):
            if trapVector[trapVectorIndex] == 1:
                costVector[trapVectorIndex] += 0
        print("Cost vector : " + str(costVector))
        return costVector



    def applyTrapVectorToMatrix(self,trapVector):

        for trapVectorIndex in range(1,len(trapVector)):
            if trapVector[trapVectorIndex] == 1:
                for x in range(0,len(trapVector)):
                    if self.RiskyMatrix[x][trapVectorIndex] >0:
                        temp =  self.RiskyMatrix[x][trapVectorIndex]
                        self.RiskyMatrix[x][0] += temp
                        self.RiskyMatrix[x][trapVectorIndex] = 0
    '''
    def applyRetreatToMatrix(self,trapVector,gameMode):
        if gameMode == 0:
            #Modification not circular
            for trapVectorIndex in range():
    '''

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
