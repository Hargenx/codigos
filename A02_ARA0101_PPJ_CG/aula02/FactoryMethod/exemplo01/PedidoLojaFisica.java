package exemplo01;

public class PedidoLojaFisica extends Pedido {
    @Override
    protected PedidoItem criarItem(Produto produto, int quantidade) {
        return new ItemPedidoLojaFisica(produto, quantidade);
    }
}
