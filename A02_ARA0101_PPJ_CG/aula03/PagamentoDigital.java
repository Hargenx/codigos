public class PagamentoDigital implements Pagamento {
    @Override
    public void pagar(double valor) {
        System.out.println("Processando pagamento digital de R$" + valor);
    }
}
