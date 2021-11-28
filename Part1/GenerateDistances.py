import os
from CalcDistances import CalcDistances
from GenerateTables import GenerateTables
from SaveToFile import SaveToFile


class GenerateDistance:
    def __init__(self, tableGenerator: GenerateTables) -> None:
        self.ListOfTfmCells = []
        self.saveF = SaveToFile(os.path.abspath(os.getcwd()))
        self.TableGenerator: GenerateTables = tableGenerator

    def GenerateEuclidesDistance(self, ListOfTfmCellsData, printTable = True):
        calcObject = CalcDistances()
        iterator = 0
        biggerOutputList = []
        for i in ListOfTfmCellsData:
            outputList = []
            for k in ListOfTfmCellsData:
                outputList.append(calcObject.CalcEuclides(i, k))
            iterator += 1
            biggerOutputList.append(outputList) 
        if printTable:  
            self.TableGenerator.TextTable(biggerOutputList, "Euclides.txt")
        return biggerOutputList

    def GenerateCosineDistance(self, ListOfTfmCellsData, printTable = True):
        calcObject = CalcDistances()
        iterator = 0
        biggerOutputList = []
        for i in ListOfTfmCellsData:
            outputList = []
            for k in ListOfTfmCellsData:
                outputList.append(calcObject.CalcCosine(i, k))
            iterator += 1
            biggerOutputList.append(outputList) 
        if printTable:
            self.TableGenerator.TextTable(biggerOutputList, "Cosine.txt")
        return biggerOutputList

    def GenerateChebysheveDistance(self, ListOfTfmCellsData, printTable = True):
        calcObject = CalcDistances()
        iterator = 0
        biggerOutputList = []
        for i in ListOfTfmCellsData:
            outputList = []
            for k in ListOfTfmCellsData:
                outputList.append(calcObject.CalcChebyshev(i, k))
            iterator += 1
            biggerOutputList.append(outputList) 
        if printTable:  
            self.TableGenerator.TextTable(biggerOutputList, "Chebyshev.txt")
        return biggerOutputList

    def GenerateManhatanDistance(self, ListOfTfmCellsData,  printTable = True):
        calcObject = CalcDistances()
        iterator = 0
        biggerOutputList = []
        for i in ListOfTfmCellsData:
            outputList = []
            for k in ListOfTfmCellsData:
                outputList.append(calcObject.CalcManhatan(i, k))
            iterator += 1
            biggerOutputList.append(outputList)
        if printTable:  
            self.TableGenerator.TextTable(biggerOutputList, "Manhatan.txt")
        return biggerOutputList

    def GeneratePowDistance(self,ListOfTfmCellsData,  p: int, r: int):
        calcObject = CalcDistances()
        iterator = 0
        biggerOutputList = []
        for i in ListOfTfmCellsData:
            outputList = []
            for k in ListOfTfmCellsData:
                outputList.append(calcObject.CaclPowDistance(i, k, p, r))
            iterator += 1
            biggerOutputList.append(outputList) 
        self.TableGenerator.TextTable(biggerOutputList, "Pow{}{}.txt".format(p, r))
        return biggerOutputList