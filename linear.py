import re

xValues = input("Hvad er dine x-værdier?: ")
xValuesList = [float(s) for s in re.findall(r"[-+]*\d*\.\d+|[-+]?\d*\d+", xValues)]

yValues = input("Hvad er dine y-værdier?: ")
yValuesList = [float(s) for s in re.findall(r"[-+]*\d*\.\d+|[-+]?\d*\d+", yValues)]

n = len(xValuesList)
x2ValuesList = []
xyValuesList = []
coords = []

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

a = (xySum - n*xAvg*yAvg)/(x2Sum - n*xAvg**2)
b = yAvg - a*xAvg
y = str(round(a,5))+"x + " + str(round(b,5))
print("y =", y)

q = 0
while q < len(xValuesList):
    coords.append((xValuesList[q], yValuesList[q]))
    q += 1
