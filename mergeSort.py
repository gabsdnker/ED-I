import random
def merge(A, aux, esquerda, meio, direita):
    for k in range(esquerda, direita + 1):
        aux[k] = A[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            A[k] = aux[j]
            j += 1
        elif j > direita:
            A[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1


def mergesort(A, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2
    mergesort(A, aux, esquerda, meio)
    mergesort(A, aux, meio + 1, direita)
    merge(A, aux, esquerda, meio, direita)

A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)
aux = [0] * len(A)
mergesort(A, aux, 0, len(A) - 1)
print("Arranjo ordenado:", A)