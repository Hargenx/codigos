package aula04.polimorfismo;

// Classe principal para demonstrar o uso do polimorfismo
public class PolimorfismoExemplo {
    public static void main(String[] args) {
        // Array de Funcionario contendo diferentes tipos de funcionários
        Funcionario[] Funcionarios = new Funcionario[3];

        Funcionarios[0] = new Desenvolvedor("Raphael", 40_000.0, 10, 50.0);
        Funcionarios[1] = new Gerente("Roberto", 50_000.0, 1500.0);
        Funcionarios[2] = new Estagiario("Carlos", 3_000.0);

        // Iteração polimórfica: cada objeto "sabe" como executar seus próprios métodos
        for (Funcionario emp : Funcionarios) {
            emp.servico();
            System.out.println("Salário: R$ " + emp.calcularSalario());
            System.out.println("---------------------------------");
        }
    }
}
