#Data: 22/03/2023
#Author: Gabrielli Danker   Matéria: Estrutura de Dados I
#Questão 2- Lista 1

import random

def criaVetorEmbaralhado(n):
    vetor = list(range(1, n+1)) # cria um vetor com valores de 1 a n (ou 0 a n-1)
    random.shuffle(vetor) # embaralha o vetor aleatoriamente
    return vetor
    
def main():
    n = 10
    vetor = criaVetorEmbaralhado(n)
    print(vetor)

if __name__ == '__main__':
    main()

#[3, 9, 6, 2, 5, 10, 8, 7, 1, 4] 