package A03_ARA0075_POO_NA.aula04.polimorfismo;

// Subclasse representando um estagiário
class Estagiario extends Funcionario {
    private double estipendio;

    public Estagiario(String nome, double estipendio) {
        super(nome);
        this.estipendio = estipendio;
    }

    @Override
    public void servico() {
        System.out.println("Estagiário " + nome + " está auxiliando nas tarefas.");
    }

    @Override
    public double calcularSalario() {
        // Estagiário recebe um valor fixo (bolsa)
        return estipendio;
    }
}