from scipy.spatial import distance

class CalcDistances:
    def __init__(self) -> None:
        pass

    def CalcCosine(self, list1: list, list2: list):
        return 1 - distance.cosine(list1, list2)

    def CalcEuclides(self, list1: list, list2: list):
        return distance.euclidean(list1, list2)

    def CalcChebyshev(self, list1: list, list2: list):
        return distance.chebyshev(list1, list2)

    def CalcManhatan(self, list1: list, list2: list):
        return distance.cityblock(list1, list2)
    
    def CaclPowDistance(self, list1: list, list2: list, p: int, r: int):
        difrence: float = 0
        for i in range(len(list1)):
            difrence += abs(list1[i] - list2[i])
        poweredDifrence = pow(difrence, p)
        if poweredDifrence == 0:
            return poweredDifrence
        return pow(poweredDifrence, -r)