import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int n = 10;
        List<Integer> vetor = criaVetorEmbaralhado(n);
        System.out.println(vetor);
    }
    
    public static List<Integer> criaVetorEmbaralhado(int n) {
        List<Integer> vetor = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            vetor.add(i);
        }
        Collections.shuffle(vetor, new Random());
        return vetor;
    }
}
