import string


def anythingToDecimal(x, k):
    alfabet = list(string.ascii_uppercase)
    suma = 0
    p = 0
    for i in range(len(x) - 1, -1, -1):
        if x[i].isnumeric():
            suma += int(x[i]) * k ** p
        else:
            liczba_z_litery = alfabet.index(x[i]) + 10
            suma+= liczba_z_litery * k ** p
        p += 1

    return suma

print(anythingToDecimal('EBK', 34))

