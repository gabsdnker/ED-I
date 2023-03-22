#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void criaVetorEmbaralhado(int n, int *v) {
    int i;
    for (i = 0; i < n; i++) {
        v[i] = i + 1;
    }
    srand(time(NULL));
    for (i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int aux = v[i];
        v[i] = v[j];
        v[j] = aux;
    }
}

int main() {
    int n = 10;
    int vetor[n];
    criaVetorEmbaralhado(n, vetor);
    printf("Vetor embaralhado: [ ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("]\n");
    return 0;
}
