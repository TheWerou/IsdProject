from typing import Text


class DataItem:
    def __init__(self, dataName: Text, dataPath: Text):
        self.DataName: Text = dataName
        self.DataPath: Text = dataPath