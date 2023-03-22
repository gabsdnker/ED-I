#Data: 22/03/2023
#Author: Gabrielli Danker   Matéria: Estrutura de Dados I
#Questão 3- Lista 1 

import time
import random

# função para criar vetor embaralhado
def criaVetorEmbaralhado(n):
    vetor = list(range(1, n+1)) # cria um vetor com valores de 1 a n (ou 0 a n-1)
    random.shuffle(vetor) # embaralha o vetor aleatoriamente
    return vetor

# função de ordenação Bubble Sort
def bubbleSort(n, v):
    for i in range(n-1):
        for j in range(n-i-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]

# função de ordenação Quick Sort
def quickSort(n, v):
    if n <= 1:
        return v
    else:
        pivo = v[0]
        menores = [x for x in v[1:] if x <= pivo]
        maiores = [x for x in v[1:] if x > pivo]
        return quickSort(len(menores), menores) + [pivo] + quickSort(len(maiores), maiores)

# função de ordenação Merge Sort
def mergeSort(n, v):
    if n <= 1:
        return v
    else:
        meio = n//2
        esquerda = mergeSort(meio, v[:meio])
        direita = mergeSort(n-meio, v[meio:])
        return merge(esquerda, direita)

# função auxiliar para o Merge Sort
def merge(esquerda, direita):
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
    # cria 3 vetores embaralhados de 101, 102, 103 e 104 elementos cada
    vetores = [criaVetorEmbaralhado(n) for n in [101, 102, 103, 104]]

    # ordena cada vetor com Bubble Sort, Quick Sort e Merge Sort e mede o tempo de execução
    for v in vetores:
        print(f"Vetor com {len(v)} elementos:")
        for nome_algoritmo, funcao_ordenacao in [("Bubble Sort", bubbleSort), ("Quick Sort", quickSort), ("Merge Sort", mergeSort)]:
            vetor_copia = v.copy() # cria uma cópia do vetor original
            tempo_inicio = time.time() # marca o tempo de início
            funcao_ordenacao(len(vetor_copia), vetor_copia) # ordena o vetor
            tempo_fim = time.time() # marca o tempo de fim
            tempo_decorrido = tempo_fim - tempo_inicio # calcula o tempo decorrido
            print(f"{nome_algoritmo}: {tempo_decorrido:.6f} segundos")

if __name__ == '__main__':
    main()