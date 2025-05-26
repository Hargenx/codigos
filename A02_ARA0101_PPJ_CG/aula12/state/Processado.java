package A02_ARA0101_PPJ_CG.aula12.state;

class Processado implements EstadoPedido {
    public void avancar(Pedido pedido) {
        pedido.setEstado(new Entregue());
        System.out.println("Pedido foi entregue.");
    }

    public void cancelar(Pedido pedido) {
        pedido.setEstado(null);
        System.out.println("Pedido em procesamento cancelado.");
        //System.out.println("Não é possível cancelar. Pedido já processado.");
    }
}