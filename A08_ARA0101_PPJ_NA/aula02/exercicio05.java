package A08_ARA0075_PPS_NA.aula02;

public class exercicio05 {

    public static float fatorial(int n) {
        int fat = 1;
        for (int i = 1; i <= n; i++) {
            fat *= i;
        }
        return fat;
    }
    public static void main(String[] args) {
        int n = Integer.parseInt(System.console().readLine("Digite o valor para o calculo do Fatorial: "));
        System.out.println("Fatorial de " + n +  " = " + fatorial(n));
    }
}
