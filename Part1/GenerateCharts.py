from matplotlib import pyplot as plt
import numpy as np

from sklearn.cluster import KMeans

class GenerateCharts:
    def __init__(self) -> None:
        pass

    def ShowChart(self, data, name):
        haha = np.array(data)
        wynik = self.mds(haha)
        twynik = wynik.transpose(1, 0)
        kmeans = KMeans(n_clusters=3).fit(twynik)

        wynik1 = wynik[0, :]
        wynik2 = wynik[1, :]
        plt.title(name)
        plt.scatter(wynik1, wynik2, c=kmeans.labels_, cmap='rainbow')
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