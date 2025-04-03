public class PagamentoAdapter implements Pagamento {
    private SistemaAntigo sistema;

    public PagamentoAdapter(SistemaAntigo sistema) {
        this.sistema = sistema;
    }

    public void pagar(double valor) {
        sistema.realizarPagamento(valor);
    }
}