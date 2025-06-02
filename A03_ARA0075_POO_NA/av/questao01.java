package A03_ARA0075_POO_NA.av;

public class questao01 {
    private String nome;
    private int idade;

    public questao01(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public void apresentar() {
        System.out.println("Olá, meu nome é " + nome + " e tenho " + idade + " anos.");
    }
}
