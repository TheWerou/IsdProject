from typing import Text


class TfmCell:
    def __init__(self, dateName: Text, termName: Text, amount: int) -> None:
        self.DateName: Text = dateName
        self.TermName: Text = termName
        self.Amount: int = amount