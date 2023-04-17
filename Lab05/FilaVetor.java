//NAME: GABRIELLI DANKER        CLASS: BCC 2022.3            

//Filas (com arrays)- LAB05

public class FilaVetor implements Fila {
    // atributos privados da classe FilaVetor
    private int tam;
    private int n;
    private int ini;
    private int vet[];

    public FilaVetor(int tam) {
        // método construtor da classe FilaVetor
        this.tam = tam;
        this.n = 0;
        this.ini = 0;
        this.vet = new int[tam];
    }

    // implementação dos métodos da interface Fila
    @Override
    public void enqueue(int v) throws Exception {
        if (n == tam)
            throw new Exception("Fila cheia");
        int fim = (ini + n) % tam;
        vet[fim] = v;
        n++;
    }

    @Override
    public int dequeue() throws Exception {
        if (isEmpty())
            throw new Exception("Fila vazia");
        int elem = vet[ini];
        ini = (ini + 1) % tam;
        n--;
        return elem;
    }

    @Override
    public String toString() {
        String s = "";
        int i = ini;
        for (int j = 0; j < n; j++) {
            s += vet[i] + " ";
            i = (i + 1) % tam;
        }
        return s;
    }

    @Override
    public boolean isEmpty() {
        return (n == 0);
    }

    @Override
    public void reset() {
        n = 0;
        ini = 0;
    }

    @Override
    public FilaVetor concatena(FilaVetor f2) throws Exception {
        int tamF3 = tam + f2.tam;
        FilaVetor f3 = new FilaVetor(tamF3);
        System.out.println("Fila 1: " + this.toString());
        System.out.println("Fila 2: " + f2.toString());
        for (int i = 0; i < n; i++) {
            f3.enqueue(vet[(ini + i) % tam]);
        }
        for (int i = 0; i < f2.n; i++) {
            f3.enqueue(f2.vet[(f2.ini + i) % f2.tam]);
        }
        System.out.println("Fila concatenada: " + f3.toString());
        return f3;
    }

    @Override
    public FilaVetor merge(FilaVetor f2) throws Exception {
        int tamF3 = tam + f2.tam;
        FilaVetor f3 = new FilaVetor(tamF3);
        System.out.println("Fila 1: " + this.toString());
        System.out.println("Fila 2: " + f2.toString());
        int i = 0, j = 0;
        while (i < n || j < f2.n) {
            if (i < n)
                f3.enqueue(vet[(ini + i) % tam]);
            if (j < f2.n)
                f3.enqueue(f2.vet[(f2.ini + j) % f2.tam]);
            i++;
            j++;
        }
        System.out.println("Filas mescladas: " + f3.toString());
        return f3;
    }
    public static void main(String[] args) {
        FilaVetor fila1 = new FilaVetor(5);
        FilaVetor fila2 = new FilaVetor(3);
    
        try {
            fila1.enqueue(1);
            fila1.enqueue(2);
            fila1.enqueue(3);
            fila2.enqueue(4);
            fila2.enqueue(5);
            fila2.enqueue(6);
            fila1.merge(fila2);
            fila1.concatena(fila2);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }    
}
