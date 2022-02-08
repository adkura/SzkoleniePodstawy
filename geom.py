import math

def GiveGeomSeqElement(a1 = 2, factor = 2, index = 2):
    value = a1*pow(factor, index-1)
    return value

def GiveFactorForGeomSeq(term, nextterm):
    #returns factor for geometrical sequence having two following terms of the sequence
    return nextterm/term

def GiveSumOfNElementsGeomSeq(a1 =2, factor = 2, n=2):
    sumN = a1*(1-pow(factor,n))/(1-factor)
    return sumN

