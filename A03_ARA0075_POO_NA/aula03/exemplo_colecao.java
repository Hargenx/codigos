import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Pessoa {
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public int getIdade() {
        return idade;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public String toString() {
        return "Pessoa{" +
                "nome='" + nome + '\'' +
                ", idade=" + idade +
                '}';
    }
}

public class exemplo_colecao {
    public static void main(String[] args) {
        List<Pessoa> pessoas = new ArrayList<>();
        pessoas.add(new Pessoa("Raphael", 40));
        pessoas.add(new Pessoa("Caroline", 32));
        pessoas.add(new Pessoa("Vinicius", 52));
        pessoas.add(new Pessoa("Gilson", 69));
        pessoas.add(new Pessoa("Sara", 69));

        // Agrupa as pessoas por idade
        Map<Integer, List<Pessoa>> agrupamento = pessoas.stream()
                .collect(Collectors.groupingBy(Pessoa::getIdade));

        // Exibe o resultado do agrupamento
        agrupamento.forEach((idade, lista) -> {
            System.out.println("Idade: " + idade);
            lista.forEach(pessoa -> System.out.println("   " + pessoa));
        });
    }
}
