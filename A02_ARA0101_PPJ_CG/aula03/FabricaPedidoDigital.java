public class FabricaPedidoDigital implements FabricaPedido {
    @Override
    public ItemPedido criarItemPedido(Produto produto, int quantidade) {
        return new ItemPedidoDigital(produto, quantidade);
    }

    @Override
    public Pagamento criarPagamento() {
        return new PagamentoDigital();
    }

    @Override
    public Entrega criarEntrega() {
        return new EntregaDigital();
    }
}
