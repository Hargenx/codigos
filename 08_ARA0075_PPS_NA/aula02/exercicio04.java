public class exercicio04 {
    public static void main(String[] args) {
        int [] vetor = new int[5];
        int soma = 0;
        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Digite o " + (i + 1) + "o elemento do vetor: ");
            vetor[i] = Integer.parseInt(System.console().readLine());
            soma += vetor[i];
        }
        /*for (int i = 0; i < vetor.length; i++) {
         //   
        }*/
        System.out.println("A soma dos elementos do vetor eh: " + soma);
    }
    
}
