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
from sklearn.manifold import MDS
from sklearn.cluster import KMeans

from CalcDistances import CalcDistances
from GenerateCharts import GenerateCharts
from GenerateDistances import GenerateDistance
from GenerateTables import GenerateTables
from SaveToFile import SaveToFile

class MainClass:
    def __init__(self, pdfDir):
        self.pdfDir = pdfDir
        self.terms = ["candy", "bar", "lollypop", "jelly candy", "chocolate", "ice cream", "dessert", "sweets", "hard candy", "cake", "engine", "pen"]
        self.AllFileNames = []
        self.ListOfTfmCells = []
        self.ListOfTfmCellsData = []
        self.ListOfData = self.GenerateData()
        self.ScriptDir = os.path.abspath(os.getcwd())
        self.saveF = SaveToFile(os.path.abspath(os.getcwd()))
        self.TableGenerator = GenerateTables(self.AllFileNames, self.ScriptDir, self.terms)

    def GenerateData(self):
        self.AllFileNames = self.GetAllFileNames()
        listOfData = []
        for i in self.AllFileNames:
            newData = DataItem(i, self.pdfDir + i)
            listOfData.append(newData)

        return listOfData

    def GenerateTfmCellList(self):
        for i in self.ListOfData: 
            outputList = []
            textToAnalize = self.GetExtractedText(i.DataName)
            for k in self.terms:
                tfmCell = self.CountWordFormPDF(k, textToAnalize)
                outputList.append(tfmCell)
                self.ListOfTfmCells.append(tfmCell)
            self.ListOfTfmCellsData.append(outputList)
        self.TableGenerator.TfmTextTable(self.ListOfTfmCellsData, "TFM.txt")
        
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

    def mds(self, similarity):
        model = MDS(dissimilarity='precomputed')
        # result = model.fit_transform(1 - similarity)
        result = model.fit_transform(similarity)
        return result.T

    def PrepDataToShow(self, data, nr_clasters):
        haha = np.array(data)
        wynik = self.mds(haha)
        twynik = wynik.transpose(1, 0)
        kmeans = KMeans(n_clusters=nr_clasters).fit(twynik)

        wynik1 = wynik[0, :]
        wynik2 = wynik[1, :]
        return wynik1, wynik2, kmeans.labels_



if __name__ == "__main__":
        cos = MainClass('C:\\Users\\wojte\Desktop\\notatki\\ISD\\zaj1\\PDF\\')

        cos.GenerateTfmCellList()
        generator = GenerateDistance(cos.TableGenerator)

        Euclides = generator.GenerateEuclidesDistance(cos.ListOfTfmCellsData)
        Manhatan = generator.GenerateManhatanDistance(cos.ListOfTfmCellsData)
        Cosine = generator.GenerateCosineDistance(cos.ListOfTfmCellsData)
        Chebysheve = generator.GenerateChebysheveDistance(cos.ListOfTfmCellsData)
        Pow12 = generator.GeneratePowDistance(cos.ListOfTfmCellsData, 1, 2)
        Pow34 = generator.GeneratePowDistance(cos.ListOfTfmCellsData, 3, 4)
        Pow56 = generator.GeneratePowDistance(cos.ListOfTfmCellsData, 5, 6)

        ListOfList = [Euclides, Manhatan, Cosine, Chebysheve, Pow12, Pow34, Pow56]
        ListONames = ["Euclides", "Manhatan", "Cosine", "Chebysheve", "Potegowy 1 2", "Potegowy 3 4", "Potegowy 5 6"]

        chartGenerator = GenerateCharts()
        items = []
        iterator = 0
        # for i in ListOfList:
        #     chartGenerator.ShowChart(cos.PrepDataToShow(i, 3), ListONames[iterator], cos.AllFileNames)
        #     iterator += 1

        items = []
        iterator = 0
        for i in ListOfList:
            chartGenerator.ShowChart(cos.PrepDataToShow(i, 7), ListONames[iterator], cos.AllFileNames)
            iterator += 1



