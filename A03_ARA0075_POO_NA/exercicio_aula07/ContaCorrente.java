package A03_ARA0075_POO_NA.exercicio_aula07;

public class ContaCorrente extends Conta {
    private double limite;

    public ContaCorrente(String numero, Cliente cliente, double limite) {
        super(numero, cliente);
        this.limite = limite;
    }

    @Override
    public boolean sacar(double valor) {
        if (valor > 0 && saldo + limite >= valor) {
            saldo -= valor;
            return true;
        }
        return false;
    }

    @Override
    public String getTipo() {
        return "Conta Corrente";
    }
}
