public class Main {
    public static void main(String[] args) {
        Pagamento pagamento = new PagamentoAdapter(new SistemaAntigo());
        pagamento.pagar(150.0);
    }
}
