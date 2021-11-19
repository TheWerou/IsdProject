import re
from typing import List
from GenerateDistances import GenerateDistance
from main import MainClass


class ShopSystem:
    def __init__(self) -> None:
        self.ListOfTransactions = []

    def AddTransactions(self, data):
        varToShow = len(self.ListOfTransactions) + 1
        baseList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for item in data:
            itemPosition = item[0] - int(1)
            if baseList[itemPosition] == 0:
                baseList[itemPosition] = item[1]
            else:
                baseList[itemPosition] += item[1]   

        self.ListOfTransactions.append(baseList)
    
    def GenerateDistance(self) -> List:
        cos = MainClass('C:\\Users\\wojte\Desktop\\notatki\\ISD\\zaj1\\PDF\\')
        cos.GenerateTfmCellList()
        generator = GenerateDistance(cos.TableGenerator)
        values = generator.GenerateChebysheveDistance(self.ListOfTransactions, False)
        cos.TableGenerator.TextTableEnhanced(values, "Sugestion.txt", self.GenerateLineNames(len(self.ListOfTransactions)))
        return values

    def GenerateLineNames(self, amount):
        listOfNames = []
        for i in range(amount):
            listOfNames.append("Trans{}".format(i))
        return listOfNames

    def Find3Smalest(self, data: List):
        newData = data[-1].copy()
        newData.sort()
        listElemenst = newData[1:4]
        indexList = []
        for i in listElemenst:
            itemToappend = data[-1].index(i)
            indexList.append(itemToappend)

        return indexList

    def IndexToShopItems(self, listOfIndex):
        listOfItemsIndex = []
        for i in listOfIndex:
            itemList = self.ListOfTransactions[i]
            listOfItemsIndex += self.GetItemsPosition(itemList)
        myset = set(listOfItemsIndex)
        return myset
        
    def GetItemsPosition(self, itemList):
        listOfItemsIndex = []
        iterator = 0
        for i in itemList:
            if i != 0:
                listOfItemsIndex.append(iterator)
            iterator += 1 
        return listOfItemsIndex

    def AddAndShowRecomendatedItems(self, Transaction):
        self.AddTransactions(Transaction)
        distance: List = self.GenerateDistance()
        smalestDistance = self.Find3Smalest(distance)
        itemsToSugest = self.IndexToShopItems(smalestDistance)
        return itemsToSugest