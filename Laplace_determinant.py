import random
import math
print('Podaj wielkosc macierzy, ktorej wyznacznik ma zostac obliczony')
wielkosc_macierzy=int(input())

def TworzMacierz ():


 x=[[0 for a in range(wielkosc_macierzy)] for b in range(wielkosc_macierzy)] 
 for i in range(wielkosc_macierzy):
    for j in range(wielkosc_macierzy):
         x[i][j]=random.randint(-1000,1000)

 print(x)
 return x

def Wyznacznik(x,wielkosc):


    if wielkosc==1:
        return x
    elif wielkosc==2:
        return (x[0][0]*x[1][1])-(x[1][0]*x[0][1])
    elif wielkosc>2:
        zastepcza=[[0 for a in range(wielkosc-1)] for b in range(wielkosc-1)]
        wynik=0
        
        for i in range(wielkosc):
            for j in range(wielkosc-1):
                jj=0
                for k in range(wielkosc):
                    if k==i:
                        continue
                    zastepcza[j][jj]=x[j][k]
                    jj+=1
            
            wynik=wynik+(Wyznacznik(zastepcza,wielkosc-1)*x[wielkosc-1][i])*math.pow(-1,(i+1+wielkosc))
            
        return wynik


print(Wyznacznik(TworzMacierz(),wielkosc_macierzy))

#superpozycja
#inerptrtuj postulat mchaniki kwantowej 

#for i in range(wielkosc_macierzy-1):
 #           for j in range(wielkosc_macierzy-1):
   #             if x[i][j]==0:
  #                  ilosc_zer[0]+=1
    #        if ilosc_zer[0]>ilosc_zer[1]:
     #           ilosc_zer[1]=ilosc_zer[0]