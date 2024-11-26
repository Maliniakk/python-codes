suma=0
p=1
x=0.1
while x<10:
    a = x**2/50
    b = 1+x**2/100-x/200
    bok = a+b
    suma+=(bok+p)/2*0.1
    p=bok
    x+=0.1
print(round(suma,2))
