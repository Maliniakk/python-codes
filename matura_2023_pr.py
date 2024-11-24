plik=open('anagram.txt','r')
tab=[]
for i in plik:
    tab.append(i.strip())

def z_2_10(x):
    p=0
    suma=0
    for i in range(len(x)-1,-1,-1):
        suma+=int(x[i])*2**p
        p+=1
    return suma

liczby_w_10=[]
for i in tab:
    liczby_w_10.append(z_2_10(i))

k=0
for i in liczby_w_10:
    if '0' not in str(i):
        k+=1
print(k)

max_suma=0
suma=0
max_liczba=0
for i in liczby_w_10:
    i=str(i)
    q=set(i)
    for j in q:
        suma+=int(j)
        if max_suma<suma:
            max_suma=suma
            max_liczba=i
    suma=0

print(max_liczba)
















