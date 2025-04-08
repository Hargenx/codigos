package aula10_exercicio;

public class Main {
    public static void main(String[] args) {
        ProdutoPerecivel leite = new ProdutoPerecivel(1, "Leite", 5, 4.50);
        ProdutoNaoPerecivel arroz = new ProdutoNaoPerecivel(2, "Arroz", 20, 3.00);

        MovimentacaoEstoque entradaLeite = new MovimentacaoEstoque(leite, 10, "entrada");
        MovimentacaoEstoque saidaLeite = new MovimentacaoEstoque(leite, 5, "saida");
        MovimentacaoEstoque saidaLeiteExcesso = new MovimentacaoEstoque(leite, 20, "saida");

        entradaLeite.start();
        saidaLeite.start();
        saidaLeiteExcesso.start();

        try {
            entradaLeite.join();
            saidaLeite.join();
            saidaLeiteExcesso.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        leite.exibirInformacoes();
        arroz.exibirInformacoes();
    }
}
