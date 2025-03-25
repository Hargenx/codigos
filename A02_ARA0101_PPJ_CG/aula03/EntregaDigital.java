public class EntregaDigital implements Entrega {
    @Override
    public double calcularCustoEntrega() {
        // Produtos digitais não possuem custo de entrega.
        return 0.0;
    }
}
