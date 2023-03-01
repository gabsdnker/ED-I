lista = [1,5,64,4,10]
tam= len(lista)

for i in range(0, tam-1):
    troca= 'false'

    for j in range (0, tam-1):
        if lista[j] > lista[j+1]:
            temp= lista[j]
            lista[j]= lista[j+1]
            lista[j+1]= temp
            troca= 'true'
    if troca == 'false':
        break

print (lista)