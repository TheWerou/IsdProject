import os
from prettytable import PrettyTable
from typing import Text
from ShopSystem import ShopSystem

from SaveToFile import SaveToFile

class Shop:
    def __init__(self) -> None:
        self.saveF = SaveToFile(os.path.abspath(os.getcwd()))
        self.shopSystem = ShopSystem()
        self.productNames = ["", "1.candy", "2.bar", "3.lollypop", "4.jelly candy", "5.chocolate", "6.ice cream", "7.dessert", "8.sweets", "9.hard candy", "10.cake", "11.engine", "12.pen"]
        
        test1 = [
            [0, 0, 0, 0, 4, 0, 1, 0, 0, 0, 1, 0],
            [2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
        
        test2 = [
            [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0],
            [0, 5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

        self.shopSystem.ListOfTransactions = test1

    def Main(self):
        self.TableOfProduct()
        selectedItem = self.ChoseItemToBuy()
        sugestion = self.shopSystem.AddAndShowRecomendatedItems([selectedItem])    
        self.SugestItem(sugestion)

    def TableOfProduct(self):
        x = PrettyTable()
        x.field_names = self.productNames
        dataToShow = ["Price", 1.2, 1.5, 1.1, 2.3, 5 ,6.3, 13.2, 1.45, 6.35, 4, 50 ,2.5]
        x.add_row(dataToShow) 
        print("Chose item to buy")
        print(x.get_string())

    def ChoseItemToBuy(self):  
        print("What item would you like to buy? 0 to exit")
        print("> ", end='')
        itemBuyed = int(input())
        print("What amount ")
        print("> ", end='')

        amountBuyed = int(input())

        return [itemBuyed, amountBuyed]

    def ChoseItemsToBuy(self):
        exit = True
        chosenItemList = []
        while exit:
            print("What item would you like to buy? 0 to exit")
            print("> ", end='')
            itemBuyed = int(input())
            if itemBuyed == 0:
                break
            print("What amount ")
            print("> ", end='')

            amountBuyed = int(input())
            if amountBuyed == 0:
                break
            chosenItemList.append([itemBuyed, amountBuyed])
        return chosenItemList
    
    def SugestItem(self, itemToSugest):
        print(f"Other people alsow buyed: ")
        for i in itemToSugest:
            print(self.productNames[i + 1])
            


main = Shop()
main.Main()
