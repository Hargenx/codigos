package A08_ARA0075_PPS_NA.aula07.composite;

public class ProdutoSimples implements Produto {
    private String nome;
    private double preco;

    public ProdutoSimples(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }
}