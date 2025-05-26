package A02_ARA0101_PPJ_CG.aula12.state;

class Pedido {
    private EstadoPedido estado;

    public Pedido() {
        this.estado = new Novo();
    }

    public void setEstado(EstadoPedido estado) {
        this.estado = estado;
    }

    public void avancar() {
        if (estado != null)
            estado.avancar(this);
    }

    public void cancelar() {
        if (estado != null)
            estado.cancelar(this);
    }
}