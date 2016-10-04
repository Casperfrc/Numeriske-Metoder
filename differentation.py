# Skal have fundet en bedre måde end eval

def getInputs():
    # Lav noget, så man kan skrive x^3 i stedet for x**3   
    eqInput = input("Hvad er din ligning? ")
    
    hInput = input("Hvad er din h-værdi? ")
    xInput = input("I hvilket punkt vil du finde hældningen? ")
    xmh = str(eval(xInput + "-" + hInput))
    xph = str(eval(xInput + "+" + hInput))
    calcStuff(eqInput, hInput, xInput, xmh, xph)

def calcStuff(eq, h, x0, xmh, xph):
    fxmh = eval(eq.replace("x", xmh))
    fxph = eval(eq.replace("x", xph))
    fMark = (fxph - fxmh) / (2*(float(h)))
