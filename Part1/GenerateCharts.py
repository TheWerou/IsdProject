from matplotlib import pyplot as plt
import numpy as np

from sklearn.cluster import KMeans

class GenerateCharts:
    def __init__(self) -> None:
        pass

    def ShowChart(self, data, name, pointNames):
        plt.title(name)
        plt.scatter(data[0], data[1], c=data[2], cmap='rainbow')
        for item in range(len(data[0])):
            plt.annotate(pointNames[item], (data[0][item], data[1][item]))
        plt.show()
    
    def ShowCharts(self, listOfNames, preperedDataList):
        f, axes = plt.subplots(nrows = 3, ncols = 3, sharex=True, sharey = True)
        iInc = 0
        kInc = 0
        iteration = 0
        for preperedData in preperedDataList:
            axes[iInc][kInc].scatter(preperedData[0], preperedData[1], c=preperedData[2], cmap='rainbow')
            axes[iInc][kInc].set_xlabel(listOfNames[iteration], labelpad = 5)
            for data in range(len(preperedData[0])):
                axes[iInc][kInc].annotate(data, (preperedData[0][data], preperedData[1][data]))
            kInc += 1
            iteration += 1
            if kInc == 3:
                iInc += 1
                kInc = 0

        plt.show()
    
    def ShowBigChart(listOfNames, preperedDataList):
        f, axes = plt.subplots(nrows = 3, ncols = 3, sharex=True, sharey = True)
        iInc = 0
        kInc = 0
        iteration = 0
        for preperedData in preperedDataList:
            axes[iInc][kInc].scatter(preperedData[0], preperedData[1], c=preperedData[2], cmap='rainbow')
            axes[iInc][kInc].set_xlabel(listOfNames[iteration], labelpad = 5)
            for data in range(len(preperedData[0])):
                axes[iInc][kInc].annotate(data, (preperedData[0][data], preperedData[1][data]))
            kInc += 1
            iteration += 1
            if kInc == 3:
                iInc += 1
                kInc = 0

        plt.show()