package A03_ARA0075_POO_NA.aula10_exercicio;

public class MovimentacaoEstoque extends Thread {
    private Produto produto;
    private int quantidade;
    private String tipoOperacao;

    public MovimentacaoEstoque(Produto produto, int quantidade, String tipoOperacao) {
        this.produto = produto;
        this.quantidade = quantidade;
        this.tipoOperacao = tipoOperacao;
    }

    @Override
    public void run() {
        System.out.println("Thread " + tipoOperacao + " executando...");
        try {
            if ("entrada".equalsIgnoreCase(tipoOperacao)) {
                produto.adicionarEstoque(quantidade);
            } else if ("saida".equalsIgnoreCase(tipoOperacao)) {
                produto.retirarEstoque(quantidade);
            } else {
                System.out.println("Operação desconhecida");
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Erro: " + e.getMessage());
        } finally {
            System.out.println("Operação concluída para produto: " + produto.getNome());
        }
    }
}
