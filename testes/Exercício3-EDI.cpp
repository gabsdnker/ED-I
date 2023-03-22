#include <iostream>
#include <algorithm> // para a função std::swap
#include <vector>
#include <chrono> // para medir o tempo de execução

using namespace std;

// função para criar vetor embaralhado
vector<int> criaVetorEmbaralhado(int n) {
vector<int> vetor(n);
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

// função de ordenação Bubble Sort
void bubbleSort(vector<int>& v) {
int n = v.size();
for (int i = 0; i < n-1; i++) {
for (int j = 0; j < n-i-1; j++) {
if (v[j] > v[j+1]) {
swap(v[j], v[j+1]);
}
}
}
}

// função de ordenação Quick Sort
void quickSort(vector<int>& v, int inicio, int fim) {
if (inicio < fim) {
int pivo = v[inicio];
int i = inicio + 1;
int j = fim;
while (i <= j) {
if (v[i] <= pivo) {
i++;
} else if (v[j] > pivo) {
j--;
} else {
swap(v[i], v[j]);
i++;
j--;
}
}
swap(v[inicio], v[j]);
quickSort(v, inicio, j-1);
quickSort(v, j+1, fim);
}
}

// função de ordenação Merge Sort
vector<int> mergeSort(const vector<int>& v) {
int n = v.size();
if (n <= 1) {
return v;
} else {
int meio = n / 2;
vector<int> esquerda(v.begin(), v.begin() + meio);
vector<int> direita(v.begin() + meio, v.end());
esquerda = mergeSort(esquerda);
direita = mergeSort(direita);
vector<int> resultado(n);
merge(esquerda.begin(), esquerda.end(), direita.begin(), direita.end(), resultado.begin());
return resultado;
}
}

// função auxiliar para o Merge Sort
void merge(vector<int>::const_iterator it1, vector<int>::const_iterator it1_end,
vector<int>::const_iterator it2, vector<int>::const_iterator it2_end,
vector<int>::iterator result) {
while (it1 != it1_end && it2 != it2_end) {
if (*it1 <= *it2) {
*result++ = *it1++;
} else {
*result++ = *it2++;
}
}
if (it1 != it1_end) {
copy(it1, it1_end, result);
}
if (it2 != it2_end) {
copy(it2, it2_end, result);
}
}

int main() {
// cria 3 vet