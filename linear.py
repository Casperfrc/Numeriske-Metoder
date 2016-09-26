import re

xValues = input("Hvad er dine x-værdier?: ")
xValuesList = [float(s) for s in re.findall(r"[-+]*\d*\.\d+|[-+]?\d*\d+", xValues)]

yValues = input("Hvad er dine y-værdier?: ")
yValuesList = [float(s) for s in re.findall(r"[-+]*\d*\.\d+|[-+]?\d*\d+", yValues)]
