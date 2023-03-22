#include <iostream>
#include <vector>

using namespace std;

void bubbleSort(int n, vector<int> &v) {
    // Implementação do Bubble Sort
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (v[j] > v[j + 1]) {
                swap(v[j], v[j + 1]);
            }
        }
    }
}

vector<int> quickSort(int n, vector<int> v) {
    // Implementação do Quick Sort
    if (n <= 1) {
        return v;
    } else {
        int pivo = v[0];
        vector<int> menores, maiores;
        for (int i = 1; i < n; i++) {
            if (v[i] <= pivo) {
                menores.push_back(v[i]);
            } else {
                maiores.push_back(v[i]);
            }
        }
        menores = quickSort(menores.size(), menores);
        maiores = quickSort(maiores.size(), maiores);
        menores.push_back(pivo);
        menores.insert(menores.end(), maiores.begin(), maiores.end());
        return menores;
    }
}

vector<int> mergeSort(int n, vector<int> v) {
    // Implementação do Merge Sort
    if (n <= 1) {
        return v;
    } else {
        int meio = n / 2;
        vector<int> esquerda(v.begin(), v.begin() + meio);
        vector<int> direita(v.begin() + meio, v.end());
        esquerda = mergeSort(esquerda.size(), esquerda);
        direita = mergeSort(direita.size(), direita);
        vector<int> resultado;
        int i = 0, j = 0;
        while (i < esquerda.size() && j < direita.size()) {
            if (esquerda[i] < direita[j]) {
                resultado.push_back(esquerda[i]);
                i++;
            } else {
                resultado.push_back(direita[j]);
                j++;
            }
        }
        resultado.insert(resultado.end(), esquerda.begin() + i, esquerda.end());
        resultado.insert(resultado.end(), direita.begin() + j, direita.end());
        return resultado;
    }
}

int main() {
    // aqui você pode criar um vetor de números inteiros
    // e chamar as funções de ordenação para ordená-lo
    
    // exemplo de criação de um vetor de números inteiros
    vector<int> v = {5, 2, 4, 6, 1, 3};
    
    // chamada da função bubbleSort
    bubbleSort(v.size(), v);
    cout << "BubbleSort: ";
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    
    // chamada da função quickSort
    v = quickSort(v.size(), v);
    cout << "QuickSort: ";
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
    
    // chamada da função mergeSort
    v = merge