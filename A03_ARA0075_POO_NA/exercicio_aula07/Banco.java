package A03_ARA0075_POO_NA.exercicio_aula07;

import java.util.ArrayList;
import java.util.List;

public class Banco {
    private List<Cliente> clientes;
    private List<Conta> contas;

    public Banco() {
        clientes = new ArrayList<>();
        contas = new ArrayList<>();
    }

    public void adicionarCliente(Cliente cliente) {
        clientes.add(cliente);
    }

    public Conta criarConta(Cliente cliente, String tipo, String numero) {
        Conta novaConta = null;
        if (tipo.equalsIgnoreCase("corrente")) {
            novaConta = new ContaCorrente(numero, cliente, 1000.0);
        } else if (tipo.equalsIgnoreCase("poupanca")) {
            novaConta = new ContaPoupanca(numero, cliente, 0.01);
        }

        if (novaConta != null) {
            contas.add(novaConta);
        }
        return novaConta;
    }

    public Conta buscarConta(String numero) {
        for (Conta c : contas) {
            if (c.getNumero().equals(numero))
                return c;
        }
        return null;
    }

    public void listarContas() {
        for (Conta c : contas) {
            System.out.println(c);
        }
    }
}
