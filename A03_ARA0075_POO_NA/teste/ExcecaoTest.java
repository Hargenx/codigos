package teste;
public class ExcecaoTest {
    public static void main(String[] args) {
        System.out.println(calcular());
    }

    static int calcular() {
        try {
            throw new RuntimeException("Falha");
        } catch (RuntimeException e) {
            return 10;
        } finally {
            return 20;
        }
    }
}
