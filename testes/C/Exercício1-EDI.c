#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int n, int* v) {
    // Implementação do Bubble Sort
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (v[j] > v[j+1]) {
                int temp = v[j];
                v[j] = v[j+1];
                v[j+1] = temp;
            }
        }
    }
}

void quickSort(int n, int* v) {
    // Implementação do Quick Sort
    if (n <= 1) {
        return;
    }
    else {
        int pivo = v[0];
        int* menores = malloc((n-1) * sizeof(int));
        int* maiores = malloc((n-1) * sizeof(int));
        int j = 0;
        int k = 0;
        for (int i = 1; i < n; i++) {
            if (v[i] <= pivo) {
                menores[j] = v[i];
                j++;
            }
            else {
                maiores[k] = v[i];
                k++;
            }
        }
        quickSort(j, menores);
        quickSort(k, maiores);
        int l = 0;
        for (int i = 0; i < j; i++) {
            v[l] = menores[i];
            l++;
        }
        v[l] = pivo;
        l++;
        for (int i = 0; i < k; i++) {
            v[l] = maiores[i];
            l++;
        }
        free(menores);
        free(maiores);
    }
}

void mergeSort(int n, int* v) {
    // Implementação do Merge Sort
    if (n <= 1) {
        return;
    }
    else {
        int meio = n/2;
        int* esquerda = malloc(meio * sizeof(int));
        int* direita = malloc((n-meio) * sizeof(int));
        for (int i = 0; i < meio; i++) {
            esquerda[i] = v[i];
        }
        for (int i = meio; i < n; i++) {
            direita[i-meio] = v[i];
        }
        mergeSort(meio, esquerda);
        mergeSort(n-meio, direita);
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < meio && j < n-meio) {
            if (esquerda[i] < direita[j]) {
                v[k] = esquerda[i];
                i++;
            }
            else {
                v[k] = direita[j];
                j++;
            }
            k++;
        }
        while (i < meio) {
            v[k] = esquerda[i];
            i++;
            k++;
        }
        while (j < n-meio) {
            v[k] = direita[j];
            j++;
            k++;
        }
        free(esquerda);
        free(direita);
    }
}

int main() {
    // exemplo de criação de um array de números inteiros
    int v[] = {5, 2, 4, 6, 1, 3};
    int n = sizeof(v) / sizeof(int);

    // chama as funções de ordenação
    bubbleSort(n, v);
    //quickSort(n, v);
    //mergeSort(n, v);

    // imprime o array ordenado
    for (int i = 0; i < n; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");

    return 0;
}
