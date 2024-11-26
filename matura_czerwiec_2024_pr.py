import string

alfabet=list(string.ascii_lowercase)

plik=open('slowa.txt','r')
tab=[]
for i in plik:
    tab.append(i.strip())

odwrocone=[]
noweslowo=''
for i in tab:
    for j in range(len(i)):
        index1=alfabet.index(i[j])
        index=(index1+13)%26
        nowalitera=alfabet[index]
        noweslowo+=nowalitera
    odwrocone.append(noweslowo)
    noweslowo=''

ma_wlasnosc=[]
k=0
for i in range(len(tab)):
    if tab[i]==odwrocone[i][::-1]:
        k+=1
        ma_wlasnosc.append(tab[i])

max_slowo=''
max_dlugosc=0
for i in ma_wlasnosc:
    if len(i)>max_dlugosc:
        max_dlugosc=len(i)
        max_slowo=i

print(k)
print(max_slowo)


