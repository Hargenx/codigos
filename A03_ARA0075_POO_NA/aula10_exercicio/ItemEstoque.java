package aula10_exercicio;

public abstract class ItemEstoque {
    private int id;
    private String nome;
    private int quantidade;
    private double valor;

    public ItemEstoque(int id, String nome, int quantidade, double valor) {
        this.id = id;
        this.nome = nome;
        this.quantidade = quantidade;
        this.valor = valor;
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public double getValor() {
        return valor;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public abstract void exibirInformacoes();
}
