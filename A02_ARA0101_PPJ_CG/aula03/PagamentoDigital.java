public class PagamentoDigital implements Pagamento {
    @Override
    public void processarPagamento(double valor) {
        System.out.println("Processando pagamento digital de R$" + valor);
    }
}
