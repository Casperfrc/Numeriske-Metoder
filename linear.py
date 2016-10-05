import matplotlib.pyplot as plt
import numpy as np
import re

def run():
    getCoords()

def getCoords():
    xValues = input("Hvad er dine x-værdier?: ")
    xValuesList = [float(s) for s in re.findall(r"[-+]*\d*\.\d+|[-+]?\d*\d+", xValues)]

    yValues = input("Hvad er dine y-værdier?: ")
    yValuesList = [float(s) for s in re.findall(r"[-+]*\d*\.\d+|[-+]?\d*\d+", yValues)]

    calcStuff(xValuesList, yValuesList)

def calcStuff(xList, yList):
    n = len(xList)
    x2ValuesList = []
    xyValuesList = []

    for i in xList:
        x2ValuesList.append(i**2)

    i = 0
    while i < len(xList):
        xyValuesList.append(xList[i]*yList[i])
        i += 1

    xAvg = sum(xList)/n
    yAvg = sum(yList)/n
    x2Sum = sum(x2ValuesList)
    xySum = sum(xyValuesList)

    a = (xySum - n*xAvg*yAvg)/(x2Sum - n*xAvg**2)
    b = yAvg - a*xAvg
    x = np.arange(xList[0]-5, xList[n-1]+5, 0.1)
    y = a*x + b
    print("y =", str(round(a,5))+"x +", str(round(b,5)))
    plotGraph(xList,yList,x,y,n)

def plotGraph(xList,yList,x,y,n):
    plt.xlim(xList[0]-5, xList[n-1]+5)
    plt.ylim(yList[0]-5, yList[n-1]+5)
    plt.grid(True)
    plt.plot(xList, yList, "ro")
    plt.plot(x, y)
    plt.show()
