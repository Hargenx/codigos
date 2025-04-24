package A02_ARA0101_PPJ_CG.aula02.FactoryMethod.exemplo01;

public class ItemPedidoLojaFisica implements PedidoItem {
    private Produto produto;
    private int quantidade;

    public ItemPedidoLojaFisica(Produto produto, int quantidade) {
        this.produto = produto;
        this.quantidade = quantidade;
    }

    @Override
    public Produto getProduto() {
        return produto;
    }

    @Override
    public int getQuantidade() {
        return quantidade;
    }

    @Override
    public double getPreco() {
        // Exemplo: preço base sem frete
        return produto.getPrecoBase() * quantidade;
    }
}
