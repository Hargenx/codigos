// Classe abstrata, serve de "molde"
abstract class ContaBancaria {
    protected double saldo;

    public ContaBancaria(double saldoInicial) {
        this.saldo = saldoInicial;
    }

    public double getSaldo() {
        return saldo;
    }

    // Métodos abstratos obrigam cada subclasse a ter sua própria implementação
    public abstract void depositar(double valor);

    public abstract void sacar(double valor);
}

// Subclasse que herda de ContaBancaria
class ContaCorrente extends ContaBancaria {
    public ContaCorrente(double saldoInicial) {
        super(saldoInicial);
    }

    @Override
    public void depositar(double valor) {
        saldo += valor;
    }

    @Override
    public void sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
        } else {
            System.out.println("Saldo insuficiente na Conta Corrente.");
        }
    }
}

// Outra subclasse que herda de ContaBancaria
class ContaPoupanca extends ContaBancaria {
    private double taxaJuros; // Ex.: 0.01 = 1% de juros

    public ContaPoupanca(double saldoInicial, double taxaJuros) {
        super(saldoInicial);
        this.taxaJuros = taxaJuros;
    }

    @Override
    public void depositar(double valor) {
        saldo += valor;
    }

    @Override
    public void sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
        } else {
            System.out.println("Saldo insuficiente na Conta Poupança.");
        }
    }

    // Método específico de ContaPoupanca
    public void renderJuros() {
        saldo += saldo * taxaJuros;
    }
}

public class Exercicios {
    public static void main(String[] args) {
        // Polimorfismo: usamos o tipo da superclasse, mas instanciamos as subclasses
        ContaBancaria cc = new ContaCorrente(1000.0);
        ContaBancaria cp = new ContaPoupanca(500.0, 0.01);

        cc.depositar(200); // Depósito na CC
        cp.depositar(200); // Depósito na CP

        System.out.println("Saldo Conta Corrente: " + cc.getSaldo());
        System.out.println("Saldo Conta Poupança: " + cp.getSaldo());

        cc.sacar(300); // Saque na CC
        cp.sacar(100); // Saque na CP

        System.out.println("Saldo Conta Corrente (após saque): " + cc.getSaldo());
        System.out.println("Saldo Conta Poupança (após saque): " + cp.getSaldo());

        // Render juros só existe em ContaPoupanca
        if (cp instanceof ContaPoupanca) {
            ((ContaPoupanca) cp).renderJuros();
            System.out.println("Saldo Conta Poupança (após render juros): " + cp.getSaldo());
        }
    }
}
