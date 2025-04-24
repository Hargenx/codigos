package A03_ARA0075_POO_NA.aula05_interface;

public class Gerente extends Funcionario {
    private double comissao;

    public Gerente(String nome, double salarioBase, double comissao) {
        super(nome, salarioBase);
        this.comissao = comissao;
    }

    public double getComissao() {
        return this.comissao;
    }

    public void setComissao(double comissao) {
        this.comissao = comissao;
    }

    @Override
    public double calcularSalario() {
        return getSalarioBase() + getComissao();
    }
}