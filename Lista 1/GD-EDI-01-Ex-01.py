#Data: 22/03/2023
#Author: Gabrielli Danker   Matéria: Estrutura de Dados I
#Questão 1- Lista 1

def bubbleSort(n, v):
    # Implementação do Bubble Sort
    for i in range(n-1):
        for j in range(n-i-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]

def quickSort(n, v):
    # Implementação do Quick Sort
    if n <= 1:
        return v
    else:
        pivo = v[0]
        menores = [x for x in v[1:] if x <= pivo]
        maiores = [x for x in v[1:] if x > pivo]
        return quickSort(len(menores), menores) + [pivo] + quickSort(len(maiores), maiores)

def mergeSort(n, v):
    # Implementação do Merge Sort
    if n <= 1:
        return v
    else:
        meio = n//2
        esquerda = mergeSort(meio, v[:meio])
        direita = mergeSort(n-meio, v[meio:])
        return merge(esquerda, direita)

def merge(esquerda, direita):
    # Função auxiliar para o Merge Sort
    i = j = 0
    resultado = []
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado

def main():
    # aqui você pode criar um array de números inteiros
    # e chamar as funções de ordenação para ordená-lo
    
    # exemplo de criação de um array de números inteiros
    v = [5, 2, 4, 6, 1, 3]
    
    # chamada da função bubbleSort
    bubbleSort(len(v), v)
    print("BubbleSort:", v)
    
    # chamada da função quickSort
    quickSort(len(v), v)
    print("QuickSort:", v)
    
    # chamada da função mergeSort
    mergeSort(len(v), v)
    print("MergeSort:", v)
    
if __name__ == '__main__':
    main()
