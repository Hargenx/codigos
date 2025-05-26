package A08_ARA0075_PPS_NA.aula06;

import java.util.Arrays;

public class ExemploClone {
    public static void main(String[] args) {
        // Exemplo 1: Atribuição simples (shallow copy por referência)
        int[] a = {3, 4, 1};
        int[] b = a;  // b aponta para o mesmo array de a
        b[0] = 9;   // Modifica o array referenciado por b

        System.out.println("Exemplo 1:");
        System.out.println("B: " + Arrays.toString(b));  // Exibe [9, 4, 1]
        System.out.println("A: " + Arrays.toString(a));  // Também exibe [9, 4, 1]

        // Exemplo 2: Clonando o array (cópia independente)
        int[] c = {3, 4, 1};
        int[] d = c.clone();  // d é uma cópia independente de c
        d[0] = 9;  // Modifica apenas o array d

        System.out.println("\nExemplo 2:");
        System.out.println("D: " + Arrays.toString(d));  // Exibe [9, 4, 1]
        System.out.println("C: " + Arrays.toString(c));  // Exibe [3, 4, 1]
    }
}