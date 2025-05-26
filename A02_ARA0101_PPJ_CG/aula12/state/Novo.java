package A02_ARA0101_PPJ_CG.aula12.state;

class Novo implements EstadoPedido {
    public void avancar(Pedido pedido) {
        pedido.setEstado(new Processado());
        System.out.println("Pedido agora está em processamento.");
    }

    public void cancelar(Pedido pedido) {
        pedido.setEstado(null);
        System.out.println("Pedido cancelado.");
    }
}