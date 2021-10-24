"""Module consisting functions that based on the principle of logic gates"""

def AND(a,b): # AND function based on the principle of AND gate i.e., returns 1 if both inputs are 1
    if a==1 and b==1:
    	return 1
    else:
    	return 0
def OR(a,b): # OR function based on the principle of OR gate i.e., returns 1 atleast one input is 1
    if a==1 or b==1:
    	return 1
    else:
    	return 0
def XOR(a,b): # XOR function based on the principle of XOR gate i.e., returns 1 when only one input is 1
    if (a != b) and (a ==1 or b==1):
    	return 1
    else:
    	return 0
def NOT(bit): # NOT function based on the principle of NOT gate i.e, returns 0 if input is 1 and vice versa
    if bit==1:
    	return 0
    if bit==0: 
    	return 1
def NAND(a,b): # NAND function based upon NOT and AND gate i.e., AND gate followed by a NOT gate 
    return NOT(AND(a,b))
    
def NOR(a,b): # NOR function based upon NOT and OR gate i.e., AND gate followed by a NOT gate 
    return NOT(OR(a,b))
