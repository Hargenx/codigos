package exemplo01;

public class PedidoOnline extends Pedido {
    @Override
    protected PedidoItem criarItem(Produto produto, int quantidade) {
        return new ItemPedidoOnline(produto, quantidade);
    }
}
