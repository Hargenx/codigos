package aula04.polimorfismo;

// Subclasse representando um desenvolvedor
class Desenvolvedor extends Funcionario {
    private double salarioBase;
    private int horasExtras;
    private double taxaHoraExtra;

    public Desenvolvedor(String nome, double salarioBase, int horasExtras, double taxaHoraExtra) {
        super(nome);
        this.salarioBase = salarioBase;
        this.horasExtras = horasExtras;
        this.taxaHoraExtra = taxaHoraExtra;
    }

    @Override
    public void servico() {
        System.out.println("Desenvolvedor " + nome + " está escrevendo código.");
    }

    @Override
    public double calcularSalario() {
        // Salário base + pagamento por horas extras
        return salarioBase + (horasExtras * taxaHoraExtra);
    }
}