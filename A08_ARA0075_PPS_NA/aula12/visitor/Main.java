package A08_ARA0075_PPS_NA.aula12.visitor;

// Elemento
interface Cliente {
    void aceitar(RelatorioClienteVisitor visitor);
}

// Elementos concretos
class PessoaFisica implements Cliente {
    String nome;
    String cpf;
    public PessoaFisica(String nome, String cpf) {
        this.nome = nome;
        this.cpf = cpf;
    }

    public void aceitar(RelatorioClienteVisitor visitor) {
        visitor.visitar(this);
    }
}

class PessoaJuridica implements Cliente {
    String razaoSocial;
    String cnpj;
    public PessoaJuridica(String razao, String cnpj) {
        this.razaoSocial = razao;
        this.cnpj = cnpj;
    }

    public void aceitar(RelatorioClienteVisitor visitor) {
        visitor.visitar(this);
    }
}

// Visitor
interface RelatorioClienteVisitor {
    void visitar(PessoaFisica pf);
    void visitar(PessoaJuridica pj);
}

// Visitor concreto
class GeradorRelatorio implements RelatorioClienteVisitor {
    public void visitar(PessoaFisica pf) {
        System.out.println("Relatório PF: " + pf.nome + ", CPF: " + pf.cpf);
    }

    public void visitar(PessoaJuridica pj) {
        System.out.println("Relatório PJ: " + pj.razaoSocial + ", CNPJ: " + pj.cnpj);
    }
}

// Main
public class Main {
    public static void main(String[] args) {
        Cliente cliente1 = new PessoaFisica("Raphael", "123.456.789-00");
        Cliente cliente2 = new PessoaJuridica("Empresa X", "12.345.678/0001-90");

        RelatorioClienteVisitor relatorio = new GeradorRelatorio();

        cliente1.aceitar(relatorio);
        cliente2.aceitar(relatorio);
    }
}