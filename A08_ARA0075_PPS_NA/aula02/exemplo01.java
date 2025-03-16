
public class exemplo01 {
    public static int Soma(int a, int b) {
        return a + b;
    }

    public static float Soma(float a, float b) {
        return a + b;
    }

    public static double Soma(double a, double b) {
        return a + b;
    }

    public static long Soma(long a, long b) {
        return a + b;
    }

    public static void main(String[] args) {
        int soma1 = Soma(1, 2);
        float soma2 = Soma(1.0f, 2.0f);
        double soma3 = Soma(1.0, 2.0);
        long soma4 = Soma(1L, 2L);
        System.out.println(soma1);
        System.out.println(soma2);
        System.out.println(soma3);
        System.out.println(soma4);
    }
}