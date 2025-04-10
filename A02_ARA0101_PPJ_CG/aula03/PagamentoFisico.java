public class PagamentoFisico implements Pagamento {
    @Override
    public void pagar(double valor) {
        System.out.println("Processando pagamento físico de R$" + valor);
    }
}
