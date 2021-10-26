from random import *
inimesed=["A","B"]
palgad=[1200,2000]

def sisesta_andmed(i,p):
    global N
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

def kustutamine(i,p):
    nimi=input("sisesta nimi, keda vaja kustutada")
    n=i.count(nimi) #кол-во
    abi_list=[]
    if n>0:
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(e) # список индексов
                print(t,".",i[e],"-",p[e])
        palk=int(input("Порядковый номер:"))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)





    return(i,p)
while 1:
    print("a-andmete sisetamine\ne andmed ekranile")
    valik=input()    
    if valik.lower()=="a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimesed,palgad)
    elif valik=="k":
            andmed_ekranile(inimesed,palgad)
    elif valik=="k":
       inimesed,palgad=kustutamine(inimesed,palgad)
    else:
        break
            



inimesed,palgad=sisesta_andmed(inimesed,palgad)
andmed_ekranile(inimesed,palgad)








