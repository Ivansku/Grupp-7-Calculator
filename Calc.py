# -*- coding: cp1252 -*-
def mathPlus(a, b):
    
    return a + b

def mathMinus(a ,b):

    return a - b

def mathMulti(a, b):

    return a * b

def mathDiv(a, b):

    return a / b

def mathAvg(a, b):

    return (a + b)/2

def mathRaised(a, b):
    return a**b

#variabler för median värdet om större eller mindre
def bigger(a, b):
    if a > b:
        return a
    else:
        return b
def smaller (a, b):
    if a < b:
        return a
    else:
        return b
    
#själva inputen för medianen
def mathMed(a, b, c):
    if a > bigger(b, c):
        return bigger(b, c)
    else:
        if a < smaller(b, c):
            return smaller(b, c)
        else:
            return a
        if a == b or c:
            return a
