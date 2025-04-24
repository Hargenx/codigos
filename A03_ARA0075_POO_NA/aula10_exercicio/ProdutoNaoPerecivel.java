package A03_ARA0075_POO_NA.aula10_exercicio;

public class ProdutoNaoPerecivel extends Produto {
    public ProdutoNaoPerecivel(int id, String nome, int quantidade, double valor) {
        super(id, nome, quantidade, valor);
    }

    @Override
    public void exibirInformacoes() {
        System.out.println(
                "[Não Perecível] " + getNome() + " - Quantidade: " + getQuantidade() + " - Valor: " + getValor());
    }
}
