# -*- coding: cp1252 -*-
"""
Este script permite revisar no sólo si una palabra es un palíndromo, sino si una
oración es palindrómica
"""

def Pali(s):
    j = s.lower()
    r = j.replace(" ","")
    s = r
    pal = False
    if len(s)%2:
        for i in range(int(len(s)/2)):
            j = 0
            if s[-(1+j)] == s[j]:
                pal = True
            else:
                pal = False
                break
            j+=1
    else:
        for i in range(int((len(s)-1)/2)):
            j = 0
            if s[-(1+j)] == s[j]:
                pal = True
            else:
                pal = False
                break
            j+=1
    return pal

cadena = input("Agrega tu cadena")
print(Pali(cadena))
