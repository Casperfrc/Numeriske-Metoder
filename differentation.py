# Skal have fundet en bedre måde end eval

def getInputs():
    # Lav noget, så man kan skrive x^3 i stedet for x**3   
    eqInput = input("Hvad er din ligning? ")
    
    hInput = input("Hvad er din h-værdi? ")
    xInput = input("I hvilket punkt vil du finde hældningen? ")
    xmh = str(eval(xInput + "-" + hInput))
    xph = str(eval(xInput + "+" + hInput))
    calc_stuff(eqInput, hInput, xInput, xmh, xph)
