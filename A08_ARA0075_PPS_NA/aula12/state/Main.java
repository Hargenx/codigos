package A08_ARA0075_PPS_NA.aula12.state;

interface EstadoPedido {
    void avancar(Pedido pedido);

    void cancelar(Pedido pedido);
}

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

class Processado implements EstadoPedido {
    public void avancar(Pedido pedido) {
        pedido.setEstado(new Entregue());
        System.out.println("Pedido foi entregue.");
    }

    public void cancelar(Pedido pedido) {
        System.out.println("Não é possível cancelar. Pedido já processado.");
    }
}

class Entregue implements EstadoPedido {
    public void avancar(Pedido pedido) {
        System.out.println("Pedido já está entregue.");
    }

    public void cancelar(Pedido pedido) {
        System.out.println("Não é possível cancelar. Pedido já entregue.");
    }
}

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
public class Main {
    public static void main(String[] args) {
        Pedido pedido = new Pedido();
        pedido.avancar(); // Avança para Processado
        pedido.avancar(); // Avança para Entregue
        pedido.cancelar(); // Não pode cancelar, já entregue
    }
}