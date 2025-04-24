package A03_ARA0075_POO_NA.exercicio_aula07;

public class Main {
    public static void main(String[] args) {
        Banco banco = new Banco();

        Cliente cliente1 = new Cliente("Raphael", "12345678900");
        Cliente cliente2 = new Cliente("Caroline", "98765432100");

        banco.adicionarCliente(cliente1);
        banco.adicionarCliente(cliente2);

        Conta conta1 = banco.criarConta(cliente1, "corrente", "001");
        Conta conta2 = banco.criarConta(cliente2, "poupanca", "002");

        conta1.depositar(2000);
        conta2.depositar(1000);

        System.out.println("Antes da transferência:");
        banco.listarContas();

        conta1.transferir(conta2, 500);

        System.out.println("\nDepois da transferência:");
        banco.listarContas();
    }
}
