package A08_ARA0075_PPS_NA.aula04.AbstractFactory.exemplo01;

public class PedidoLojaFisica extends Pedido {
    @Override
    protected PedidoItem criarItem(Produto produto, int quantidade) {
        return new ItemPedidoLojaFisica(produto, quantidade);
    }
}
