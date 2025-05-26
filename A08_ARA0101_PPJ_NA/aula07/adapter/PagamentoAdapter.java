package A08_ARA0075_PPS_NA.aula07.adapter;

public class PagamentoAdapter implements Pagamento {
    private SistemaAntigo sistema;

    public PagamentoAdapter(SistemaAntigo sistema) {
        this.sistema = sistema;
    }

    public void pagar(double valor) {
        sistema.realizarPagamento(valor);
    }
}