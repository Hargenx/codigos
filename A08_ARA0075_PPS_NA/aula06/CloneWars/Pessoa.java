package CloneWars;

public class Pessoa {
    private String nome;
    private Endereco endereco;

    public Pessoa(String nome, Endereco endereco) {
        this.nome = nome;
        this.endereco = endereco;
    }

    public String getNome() {
        return nome;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    // Shallow copy: copia o objeto Pessoa, mas o endereço é compartilhado.
    public Pessoa cloneShallow() {
        return new Pessoa(nome, endereco);
    }

    // Deep copy: copia o objeto Pessoa e também cria uma nova instância para
    // Endereco.
    public Pessoa cloneDeep() {
        return new Pessoa(nome, new Endereco(endereco.getRua()));
    }

    @Override
    public String toString() {
        return "Pessoa{nome='" + nome + "', endereco=" + endereco + "}";
    }
}
