from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
import sympy
# Skal have fundet en bedre måde end eval
# Kode skal fixes, så det generelt bliver mere effektivt

def getInputs():
    # Lav noget, så man kan skrive x^3 i stedet for x**3   
    eqInput = input("Hvad er din ligning? ")
    hInput = input("Hvad er din h-værdi? ")
    xInput = input("I hvilket punkt vil du finde hvor hældningen er 0? ")
    calcStuff(eqInput, hInput, xInput)

def calcStuff(eq, h, x0):
    xmh = str(eval(x0 + "-" + h))
    xph = str(eval(x0 + "+" + h))
    fxmh = eval(eq.replace("x", xmh))
    fxph = eval(eq.replace("x", xph))
    fPrime = (fxph - fxmh) / (2*(float(h)))
    Peq = parse_expr(eq)
    fAnaPrime = Peq.diff(x)
    fAnaPrime = eval(str(fAnaPrime).replace("x", x0))
    print("The value of f is calculated analyticly to", fAnaPrime)

    yList = []
    xList = []
    while float(h) > 0.005:
        h = float(h)
        h += -0.005
        if h == 0:
            break
        h = str(h)
        xmh = str(eval(x0 + "-" + h))
        xph = str(eval(x0 + "+" + h))
        fxmh = eval(eq.replace("x", xmh))
        fxph = eval(eq.replace("x", xph))
        fPrime = (fxph - fxmh) / (2*(float(h)))
        yList.append(fPrime)
        xList.append(float(x0) + float(h))
        #print("h is", h)
        #print("f Prime is",fPrime)
    print("h is", h)
    print("f prime is", fPrime)
    plotGraph(xList, yList)

def plotGraph(xList,yList):
    plt.grid(True)
    plt.plot(xList, yList)
    plt.show()

x = sympy.Symbol("x")

