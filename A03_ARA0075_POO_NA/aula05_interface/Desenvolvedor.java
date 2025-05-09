package A03_ARA0075_POO_NA.aula05_interface;

public class Desenvolvedor extends Funcionario {
    private double bonus;

    public Desenvolvedor(String nome, double salarioBase, double bonus) {
        super(nome, salarioBase);
        this.bonus = bonus;
    }

    public double getBonus() {
        return this.bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    @Override
    public double calcularSalario() {
        return getSalarioBase() + getBonus();
    }
}