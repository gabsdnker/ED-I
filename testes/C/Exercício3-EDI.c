#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// função para criar vetor embaralhado
void criaVetorEmbaralhado(int n, int *v){
    int i;
    for(i=0;i<n;i++){
        v[i] = i+1;
    }
    srand(time(NULL));
    for(i=n-1;i>0;i--){
        int j = rand()%(i+1);
        int aux = v[i];
        v[i] = v[j];
        v[j] = aux;
    }
}

// função de ordenação Bubble Sort
void bubbleSort(int n, int *v){
    int i, j;
    for(i=0;i<n-1;i++){
        for(j=0;j<n-i-1;j++){
            if(v[j] > v[j+1]){
                int aux = v[j];
                v[j] = v[j+1];
                v[j+1] = aux;
            }
        }
    }
}

// função de ordenação Quick Sort
void quickSort(int *v, int ini, int fim){
    if(ini < fim){
        int pivo = v[ini], i = ini+1, j = fim;
        while(i <= j){
            if(v[i] <= pivo) i++;
            else if(v[j] > pivo) j--;
            else{
                int aux = v[i];
                v[i] = v[j];
                v[j] = aux;
                i++;
                j--;
            }
        }
        v[ini] = v[j];
        v[j] = pivo;
        quickSort(v, ini, j-1);
        quickSort(v, j+1, fim);
    }
}

// função de ordenação Merge Sort
void merge(int *v, int ini, int meio, int fim){
    int *aux, i = ini, j = meio+1, k = 0;
    aux = (int*) malloc(sizeof(int)*(fim-ini+1));
    while(i <= meio && j <= fim){
        if(v[i] <= v[j]){
            aux[k] = v[i];
            i++;
        } else {
            aux[k] = v[j];
            j++;
        }
        k++;
    }
    while(i <= meio){
        aux[k] = v[i];
        i++;
        k++;
    }
    while(j <= fim){
        aux[k] = v[j];
        j++;
        k++;
    }
    for(i=ini, k=0;i<=fim;i++, k++){
        v[i] = aux[k];
    }
    free(aux);
}

void mergeSort(int *v, int ini, int fim){
    if(ini < fim){
        int meio = (ini+fim)/2;
        mergeSort(v, ini, meio);
        mergeSort(v, meio+1, fim);
        merge(v, ini, meio, fim);
    }
}

int main(){
    int i, j, k;
    int n[4] = {101, 102, 103, 104};
    int *vetores[4];
    for(i=0;i<4;i++){
        vetores[i] = (int*) malloc(sizeof(int)*n[i]);
        criaVetorEmbaralhado(n[i], vetores[i]);
    }
    for(k=0;k<4;k++){
        printf("Vetor com %d elementos:\n", n[4]);
for(i=0;i<n[k];i++){
printf("%d ", vetores[k][i]);
}
printf("\n\n");
    // ordenação com Bubble Sort
    bubbleSort(n[k], vetores[k]);
    printf("Vetor ordenado com Bubble Sort:\n");
    for(i=0;i<n[k];i++){
        printf("%d ", vetores[k][i]);
    }
    printf("\n\n");

    // ordenação com Quick Sort
    quickSort(vetores[k], 0, n[k]-1);
    printf("Vetor ordenado com Quick Sort:\n");
    for(i=0;i<n[k];i++){
        printf("%d ", vetores[k][i]);
    }
    printf("\n\n");

    // ordenação com Merge Sort
    mergeSort(vetores[k], 0, n[k]-1);
    printf("Vetor ordenado com Merge Sort:\n");
    for(i=0;i<n[k];i++){
        printf("%d ", vetores[k][i]);
    }
    printf("\n\n");

    free(vetores[k]);
}

return 0;
}