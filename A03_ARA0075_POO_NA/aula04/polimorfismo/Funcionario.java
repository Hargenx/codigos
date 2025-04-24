package A03_ARA0075_POO_NA.aula04.polimorfismo;

// Classe abstrata representando um funcionário
abstract class Funcionario {
    protected String nome;

    public Funcionario(String nome) {
        this.nome = nome;
    }

    // Método abstrato para representar a atividade de trabalho do funcionário
    public abstract void servico();

    // Método abstrato para calcular o salário do funcionário
    public abstract double calcularSalario();
}