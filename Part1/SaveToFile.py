from typing import Text


class SaveToFile:
    def __init__(self, path: Text) -> None:
        self.FilesPath: Text = path

    def CreateAndSaveFileToText(self, fileName: Text, textToSave: Text):
        with open(self.FilesPath + '\\Data\\' + fileName, 'w', encoding='utf-8') as file:
            file.write(textToSave)

    def ReadFile(self, fileName: Text):
        with open(self.FilesPath + '\\Data\\' + fileName, 'r', encoding='utf-8') as file:
            return file.read()
