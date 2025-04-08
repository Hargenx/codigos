package aula10_exercicio;

public class ProdutoPerecivel extends Produto {
    public ProdutoPerecivel(int id, String nome, int quantidade, double valor) {
        super(id, nome, quantidade, valor);
    }

    @Override
    public void exibirInformacoes() {
        System.out
                .println("[Perecível] " + getNome() + " - Quantidade: " + getQuantidade() + " - Valor: " + getValor());
    }
}
