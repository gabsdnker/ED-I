//NAME: GABRIELLI DANKER        CLASS: BCC 2022.3 

public interface Fila {
     // interface da Fila (métodos públicos)
    public void enqueue(int v) throws Exception;
    public int dequeue() throws Exception;
    public String toString();
    public boolean isEmpty();
    public void reset();
    public FilaVetor concatena(FilaVetor f2) throws Exception;
    public FilaVetor merge(FilaVetor f2) throws Exception;
}
