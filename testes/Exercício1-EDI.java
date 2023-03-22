import java.util.Arrays;

public class SortAlgorithms {
    public static void bubbleSort(int[] v) {
    // Implementação do Bubble Sort
    int n = v.length;
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

public static int[] quickSort(int[] v) {
    // Implementação do Quick Sort
    int n = v.length;
    if (n <= 1) {
        return v;
    } else {
        int pivo = v[0];
        int[] menores = Arrays.stream(v).filter(x -> x <= pivo).toArray();
        int[] maiores = Arrays.stream(v).filter(x -> x > pivo).toArray();
        return concatenate(quickSort(menores), pivo, quickSort(maiores));
    }
}

public static int[] mergeSort(int[] v) {
    // Implementação do Merge Sort
    int n = v.length;
    if (n <= 1) {
        return v;
    } else {
        int meio = n/2;
        int[] esquerda = Arrays.copyOfRange(v, 0, meio);
        int[] direita = Arrays.copyOfRange(v, meio, n);
        return merge(mergeSort(esquerda), mergeSort(direita));
    }
}

public static int[] merge(int[] esquerda, int[] direita) {
    // Função auxiliar para o Merge Sort
    int i = 0;
    int j = 0;
    int[] resultado = new int[esquerda.length + direita.length];
    int k = 0;
    while (i < esquerda.length && j < direita.length) {
        if (esquerda[i] < direita[j]) {
            resultado[k] = esquerda[i];
            i++;
        } else {
            resultado[k] = direita[j];
            j++;
        }
        k++;
    }
    while (i < esquerda.length) {
        resultado[k] = esquerda[i];
        i++;
        k++;
    }
    while (j < direita.length) {
        resultado[k] = direita[j];
        j++;
        k++;
    }
    return resultado;
}

public static int[] concatenate(int[] a, int x, int[] b) {
    // Função auxiliar para o Quick Sort
    int[] result = new int[a.length + 1 + b.length];
    System.arraycopy(a, 0, result, 0, a.length);
    result[a.length] = x;
    System.arraycopy(b, 0, result, a.length + 1, b.length);
    return result;
}

public static void main(String[] args) {
    // aqui você pode criar um array de números inteiros
    // e chamar as funções de ordenação para ordená-lo
    
    // exemplo de criação de um array de números inteiros
    int[] v = {5, 2, 4, 6, 1, 3};
    
    // chamada da função bubbleSort
    bubbleSort(v);
    System.out.println("BubbleSort: " + Arrays.toString(v));
    
    // chamada da função quickSort
    int[] v1 = quickSort(v);
    System.out.println("QuickSort: " + Arrays)
}