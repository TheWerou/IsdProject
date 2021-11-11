import os
import sys
import re
import time
import PyPDF2
from typing import Text
from prettytable import PrettyTable
from ExtractText import ExtractText
from Model.DataItem import DataItem 
from Model.TfmCell import TfmCell
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt

from CalcDistances import CalcDistances
from SaveToFile import SaveToFile

class MainClass:
    def __init__(self):
        self.pdfDir = 'C:\\Users\\wojte\Desktop\\notatki\\ISD\\zaj1\\PDF\\'
        self.terms = ["candy", "bar", "lollypop", "jelly candy", "chocolate", "ice cream", "dessert", "sweets", "hard candy", "cake", "engine", "pen"]
        self.AllFileNames = []
        self.ListOfTfmCells = []
        self.ListOfTfmCellsData = []
        self.ListOfData = self.GenerateData()
        self.ScriptDir = os.path.abspath(os.getcwd())
        self.saveF = SaveToFile(os.path.abspath(os.getcwd()))

    def GenerateData(self):
        self.AllFileNames = self.GetAllFileNames()
        listOfData = []
        for i in self.AllFileNames:
            newData = DataItem(i, self.pdfDir + i)
            listOfData.append(newData)

        return listOfData

    def GetAllFileNames(self):
        return os.listdir(self.pdfDir)

    def CountWordFormPDF(self, word: Text, data: Text):
        totalWords = 0
        totalWords += len(re.findall(word, data))
        return totalWords

    def ExtractText(self):
        for i in self.ListOfData:
            reddedText = ExtractText(i.DataPath)
            fileName =  os.path.splitext(i.DataName)[0]
            filePath = fileName + '.txt'
            numPages = reddedText.GetNumberOfPages()
            textToSave: Text = ""
            for i in range(numPages):
                textToSave += reddedText.GetTextFromPage(i)
            self.saveF.CreateAndSaveFileToText(filePath, textToSave)

    def GetExtractedText(self, fileName: Text):
        fileNameTxt = os.path.splitext(fileName)[0] + '.txt'
        return self.saveF.ReadFile(fileNameTxt)

    def GenerateTfmCellList(self):
        for i in self.ListOfData: # tu text
            outputList = []
            textToAnalize = self.GetExtractedText(i.DataName)
            for k in self.terms:
                tfmCell = self.CountWordFormPDF(k, textToAnalize)
                outputList.append(tfmCell)
                self.ListOfTfmCells.append(tfmCell)
            self.ListOfTfmCellsData.append(outputList)

    def GenerateEuclidesDistance(self):
        calcObject = CalcDistances()
        iterator = 0
        biggerOutputList = []
        for i in self.ListOfTfmCellsData:
            outputList = []
            for k in self.ListOfTfmCellsData:
                outputList.append(calcObject.CalcEuclides(i, k))
            iterator += 1
            biggerOutputList.append(outputList) 
        self.TextTable(biggerOutputList, "Euclides.txt")

    def GenerateCosineDistance(self):
        calcObject = CalcDistances()
        iterator = 0
        biggerOutputList = []
        for i in self.ListOfTfmCellsData:
            outputList = []
            for k in self.ListOfTfmCellsData:
                outputList.append(calcObject.CalcCosine(i, k))
            iterator += 1
            biggerOutputList.append(outputList) 
        self.TextTable(biggerOutputList, "Cosine.txt")

    def GenerateChebysheveDistance(self):
        calcObject = CalcDistances()
        iterator = 0
        biggerOutputList = []
        for i in self.ListOfTfmCellsData:
            outputList = []
            for k in self.ListOfTfmCellsData:
                outputList.append(calcObject.CalcChebyshev(i, k))
            iterator += 1
            biggerOutputList.append(outputList) 
        self.TextTable(biggerOutputList, "Chebyshev.txt")

    def GenerateManhatanDistance(self):
        calcObject = CalcDistances()
        iterator = 0
        biggerOutputList = []
        for i in self.ListOfTfmCellsData:
            outputList = []
            for k in self.ListOfTfmCellsData:
                outputList.append(calcObject.CalcManhatan(i, k))
            iterator += 1
            biggerOutputList.append(outputList) 
        self.TextTable(biggerOutputList, "Manhatan.txt")

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



cos = MainClass()
# os.ExtractText()
cos.GenerateTfmCellList()
cos.GenerateEuclidesDistance()
cos.GenerateManhatanDistance()
cos.GenerateCosineDistance()
cos.GenerateChebysheveDistance()
