def quickSort (lista, a, b):
    if a < b:
        indicePivo= particiona(lista, a, b)
        quickSort(lista, a, indicePivo-1)
        quickSort(lista, indicePivo+1, b)


def particiona(lista, a, b):
    x= lista[a]
    while a < b:
        while lista[a] < x:
            a+=1
        while lista[b] > x:
            b-=1
        troca(lista, a, b)
    return a

def troca(lista, a, b):
    temp= lista[a]
    lista[a]= lista[b]
    lista[b]= temp
    
lista= [2,8,10,3,1]
tamanho= len(lista)
quickSort(lista, 0, tamanho-1)
print(lista)














