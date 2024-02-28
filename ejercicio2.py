"""
a = cantidad de mayusculas
b = cantidad de minusculas
c = cantidad de digitos
"""

import random as rd

def Contra(a,b,c,pwd = ""):
    letrasm = "a b c d e f g h i j k l m n o p q r s t w x y z".split()
    letrasM = "a b c d e f g h i j k l m n o p q r s t w x y z".upper().split()
    i, j, k = 0, 0, 0
    while len(pwd)<(a+b+c):
        rd.shuffle(letrasm)
        rd.shuffle(letrasM)
        i1 = str(rd.randint(0,9))
        i2 = letrasm[0]
        i3 = letrasM[0]
        if i<c:
            pwd += i1
            i+=1
        if j<a:
            pwd += i3
            j+=1
        if k<b:
            pwd += i2
            k+=1
    return pwd
        
    
