import java.util.Random;

public class Main {
  
  public static void main(String[] args) {
    int[] vetor = criaVetorEmbaralhado(10);
    
    System.out.println("Vetor original:");
    imprimirVetor(vetor);
    
    bubbleSort(vetor);
    System.out.println("Vetor ordenado pelo Bubble Sort:");
    imprimirVetor(vetor);
    
    vetor = criaVetorEmbaralhado(10);
    quickSort(vetor, 0, vetor.length - 1);
    System.out.println("Vetor ordenado pelo Quick Sort:");
    imprimirVetor(vetor);
    
    vetor = criaVetorEmbaralhado(10);
    mergeSort(vetor, 0, vetor.length - 1);
    System.out.println("Vetor ordenado pelo Merge Sort:");
    imprimirVetor(vetor);
  }
  
  // função para criar vetor embaralhado
  public static int[] criaVetorEmbaralhado(int n) {
    int[] vetor = new int[n];
    for (int i = 0; i < n; i++) {
      vetor[i] = i + 1;
    }
    randomizarVetor(vetor);
    return vetor;
  }

  // função para randomizar os elementos do vetor
  public static void randomizarVetor(int[] vetor) {
    Random random = new Random();
    for (int i = vetor.length - 1; i > 0; i--) {
      int j = random.nextInt(i + 1);
      int temp = vetor[i];
      vetor[i] = vetor[j];
      vetor[j] = temp;
    }
  }

  // função de ordenação Bubble Sort
  public static void bubbleSort(int[] v) {
    int n = v.length;
    for (int i = 0; i < n - 1; i++) {
      for (int j = 0; j < n - i - 1; j++) {
        if (v[j] > v[j + 1]) {
          int temp = v[j];
          v[j] = v[j + 1];
          v[j + 1] = temp;
        }
      }
    }
  }

  // função de ordenação Quick Sort
  public static void quickSort(int[] v, int inicio, int fim) {
    if (inicio < fim) {
      int pivo = particionar(v, inicio, fim);
      quickSort(v, inicio, pivo - 1);
      quickSort(v, pivo + 1, fim);
    }
  }

  // função auxiliar para o Quick Sort
  public static int particionar(int[] v, int inicio, int fim) {
    int pivo = v[inicio];
    int i = inicio + 1;
    int j = fim;
    while (i <= j) {
      if (v[i] <= pivo) {
        i++;
      } else if (v[j] > pivo) {
        j--;
      } else {
        int temp = v[i];
        v[i] = v[j];
        v[j] = temp;
        i++;
        j--;
      }
    }
    v[inicio] = v[j];
    v[j] = pivo;
    return j;
  }

  // função de ordenação Merge Sort
  public static void mergeSort(int[] v, int inicio, int fim) {
    if (inicio < fim) {
      int meio  = (inicio + fim) / 2;
    mergeSort(v, inicio, meio);
    mergeSort(v, meio + 1, fim);
    merge(v, inicio, meio, fim);
    }

// função auxiliar para o Merge Sort
public static void merge(int[] v, int inicio, int meio, int fim) {
        int[] temp = new int[fim - inicio + 1];
        int i = inicio;
        int j = meio + 1;
        int k = 0;
        while (i <= meio && j <= fim) {
            if (v[i] < v[j]) {
            temp[k] = v[i];
            i++;
           } 
            else {
            temp[k] = v[j];
            j++;
            }
              k++;
        }
        while (i <= meio) {
            temp[k] = v[i];
            i++;
            k++;
            }
        while (j <= fim) {
            temp[k] = v[j];
            j++;
            k++;
            }
        for (int p = 0; p < temp.length; p++) {
            v[inicio + p] = temp[p];
            }
        }

// função para imprimir o vetor
public static void imprimirVetor(int[] v) {
    for (int i = 0; i < v.length; i++) {
    System.out.print(v[i] + " ");
    }
    System.out.println();
}
}
}