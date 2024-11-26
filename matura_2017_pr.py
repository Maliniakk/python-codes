plik=open('binarne.txt','r')
tab=[]
for i in plik:
    tab.append(i.strip())

def BCD(x):
    slowo = ''
    k = 1
    BCD = []
    for i in range(len(x)):
        if k<4:
            slowo += x[i]
        if k==4:
            slowo += x[i]
            BCD.append(slowo)
            k=0
            slowo = ''
        k+=1
    return BCD

def z_2_na_10(x):
    p=0
    suma=0
    for i in range(len(x)-1,-1,-1):
        suma+=int(x[i])*2**p
        p+=1
    return suma

k=0
niepoprawne=[]
for i in tab:
    bcd=BCD(i)
    for j in bcd:
        if z_2_na_10(j)>9:
            k+=1
            niepoprawne.append(i)
            break

min_slowo=100000000
for i in niepoprawne:
    if len(i)<min_slowo:
        min_slowo=len(i)
print(min_slowo)
print(k)
