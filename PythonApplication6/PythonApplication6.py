from random import *
inimesed=["A","B"]
palgad=[1200,2000]

def sisesta_andmed(i,p):
    N=4
    for n in range (N):
        inimene=input("Nimi:")
        i.append(inimene)
        palk=randint(100,1000)
        p.append(palk)
    return i,p 
def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

inimesed,palgad=sisesta_andmed(inimesed,palgad)
andmed_ekranile(inimesed,palgad)








