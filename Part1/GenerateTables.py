import os
from typing import Text

from prettytable.prettytable import PrettyTable

class GenerateTables:
    def __init__(self, allFileNames, scriptDir, terms) -> None:
        self.AllFileNames = allFileNames
        self.ScriptDir = scriptDir
        self.terms = terms

    def TextTable(self, dataToShow, fileName: Text):
        x = PrettyTable()
        x.field_names = ['Data / Data'] + self.AllFileNames
        iterator = 0
        for i in dataToShow:
            x.add_row([self.AllFileNames[iterator]] + i) 
            iterator += 1

        pathToSave = self.ScriptDir + '\\Raport\\' + fileName    

        with open(pathToSave, 'w', encoding='utf-8') as file:
            file.write(x.get_string())
    
    def TextTableEnhanced(self, dataToShow, fileName: Text, names):
        x = PrettyTable()
        x.field_names = ['Data / Data'] + names
        iterator = 0
        for i in dataToShow:
            x.add_row([names[iterator]] + i) 
            iterator += 1

        pathToSave = self.ScriptDir + '\\Raport\\' + fileName    

        with open(pathToSave, 'w', encoding='utf-8') as file:
            file.write(x.get_string())

    def TfmTextTable(self, dataToShow, fileName: Text):
        x = PrettyTable()
        x.field_names = ['Data / Term'] + self.terms
        iterator = 0
        for i in dataToShow:
            x.add_row([self.AllFileNames[iterator]] + i) 
            iterator += 1

        pathToSave = self.ScriptDir + '\\Raport\\' + fileName    

        with open(pathToSave, 'w', encoding='utf-8') as file:
            file.write(x.get_string())