from typing import Text
import PyPDF2

class ExtractText:
    def __init__(self, filepath: Text):
        self.pdfReader: PyPDF2.PdfFileReader
        self.Open(filepath)

    def Open(self, path):
        pdfFileObj = open(path, 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    def GetNumberOfPages(self):
        return self.pdfReader.numPages

    def GetTextFromPage(self, pageNumber: int):
        pageObj = self.pdfReader.getPage(pageNumber)
        return pageObj.extractText()

    def Close(self):
        self.pdfFileObj.close()