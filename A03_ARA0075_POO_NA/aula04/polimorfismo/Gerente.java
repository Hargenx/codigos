package A03_ARA0075_POO_NA.aula04.polimorfismo;

// Subclasse representando um gerente
class Gerente extends Funcionario {
    private double salarioBase;
    private double bonus;

    public Gerente(String nome, double salarioBase, double bonus) {
        super(nome);
        this.salarioBase = salarioBase;
        this.bonus = bonus;
    }

    @Override
    public void servico() {
        System.out.println("Gerente " + nome + " está gerenciando a equipe.");
    }

    @Override
    public double calcularSalario() {
        // Salário base + bônus
        return salarioBase + bonus;
    }
}