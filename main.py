import os
import sys
import re
import time
from typing import Text
import PyPDF2
from ExtractText import ExtractText 

class MainClass:
    def __init__(self):
        self.pdfDir = 'C:\\Users\\wojte\Desktop\\notatki\\ISD\\zaj1\\PDF\\'
        self.terms = [Text]

    def GetAllFileNames(self):
        return os.listdir(self.pdfDir)

    def CountWordFormPDF(self, word: Text, pdf:Text):
        newobject = ExtractText(pdf)

        totalWords = 0
        numPages = newobject.GetNumberOfPages()
        for i in range(numPages):
            text = newobject.GetTextFromPage(i)
            totalWords += text.count(word)

        time.sleep(1)

        print (totalWords)

    def TestMain(self):
        print(self.GetAllFileNames())


cos = MainClass()
cos.TestMain()
    
    