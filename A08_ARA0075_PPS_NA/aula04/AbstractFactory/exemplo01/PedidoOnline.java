package A08_ARA0075_PPS_NA.aula04.AbstractFactory.exemplo01;

public class PedidoOnline extends Pedido {
    @Override
    protected PedidoItem criarItem(Produto produto, int quantidade) {
        return new ItemPedidoOnline(produto, quantidade);
    }
}
