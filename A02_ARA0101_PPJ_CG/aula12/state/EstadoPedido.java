package A02_ARA0101_PPJ_CG.aula12.state;

interface EstadoPedido {
    void avancar(Pedido pedido);

    void cancelar(Pedido pedido);
}