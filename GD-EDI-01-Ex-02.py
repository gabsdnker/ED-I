#Data: 22/03/2023
#Author: Gabrielli Danker   Matéria: Estrutura de Dados I
#Questão 2- Lista 1

import random

def criaVetorEmbaralhado(n):
    vetor = list(range(1, n+1))
    random.shuffle(vetor)
    return vetor

n = 10
vetor = criaVetorEmbaralhado(n)
print(vetor)

#[3, 9, 6, 2, 5, 10, 8, 7, 1, 4] 