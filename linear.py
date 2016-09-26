import re

xValues = input("Hvad er dine x-værdier?: ")
xValuesList = [float(s) for s in re.findall(r"[-+]*\d*\.\d+|[-+]?\d*\d+", xValues)]

yValues = input("Hvad er dine y-værdier?: ")
yValuesList = [float(s) for s in re.findall(r"[-+]*\d*\.\d+|[-+]?\d*\d+", yValues)]

n = len(xValuesList)
x2ValuesList = []
xyValuesList = []

for i in xValuesList:
    x2ValuesList.append(i**2)

w = 0
while w < len(xValuesList):
    xyValuesList.append(xValuesList[w]*yValuesList[w])
    w += 1

xAvg = sum(xValuesList)/n
yAvg = sum(yValuesList)/n
x2Sum = sum(x2ValuesList)
xySum = sum(xyValuesList)
