package A02_ARA0101_PPJ_CG.aula12.state;

class Entregue implements EstadoPedido {
    public void avancar(Pedido pedido) {
        System.out.println("Pedido já está entregue.");
    }

    public void cancelar(Pedido pedido) {
        System.out.println("Não é possível cancelar. Pedido já entregue.");
    }
}