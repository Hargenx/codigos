public class ContaPoupanca extends Conta {
    private double taxaJuros;

    public ContaPoupanca(String numero, Cliente cliente, double taxaJuros) {
        super(numero, cliente);
        this.taxaJuros = taxaJuros;
    }

    public void aplicarJuros() {
        saldo += saldo * taxaJuros;
    }

    @Override
    public String getTipo() {
        return "Conta Poupança";
    }
}
