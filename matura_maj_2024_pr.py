plik=open('liczby.txt','r')
plik1=plik.readlines()

wiersz1=(plik1[0].strip()).split()
wiersz2=(plik1[1].strip()).split()

wiersz_1=[]
wiersz_2=[]

for i in wiersz1:
    wiersz_1.append(int(i))
for i in wiersz2:
    wiersz_2.append(int(i))

k=0
suma=0
max_srednia=0
for i in range(len(wiersz_1)):
    for j in range(i,len(wiersz_1)):
        suma+=wiersz_1[j]
        k+=1
        if k>=50:
            srednia=suma/k
            if max_srednia<srednia:
                max_srednia=srednia
                poczatek=wiersz_1[i]
                dlugosc=k
    k=0
    suma=0

print(max_srednia)
print(dlugosc)
print(poczatek)
