#include <iostream>
#include <cstdlib> // para a função rand()
#include <ctime> // para a função time()

using namespace std;

int* criaVetorEmbaralhado(int n) {
    int* vetor = new int[n];
    for (int i = 0; i < n; i++) {
        vetor[i] = i + 1; // preenche o vetor com valores de 1 a n (ou 0 a n-1)
    }
    srand(time(NULL)); // inicializa a semente do gerador de números aleatórios
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1); // escolhe um índice aleatório entre 0 e i
        swap(vetor[i], vetor[j]); // troca o elemento i pelo elemento j
    }
    return vetor;
}

int main() {
    int n = 10;
    int* v = criaVetorEmbaralhado(n);
    for (int i = 0; i < n; i++) {
        cout << v[i] << " ";
    }
    cout << endl;
    delete[] v; // libera a memória alocada para o vetor
    return 0;
}
//Ele cria um vetor de tamanho n preenchido com valores de 1 a n, e em seguida embaralha aleatoriamente 
//os elementos do vetor usando a função rand() da biblioteca cstdlib e a função srand() da biblioteca
//ctime. Depois, ele imprime o vetor embaralhado na tela e libera a memória alocada para o vetor usando
//o operador delete[].
