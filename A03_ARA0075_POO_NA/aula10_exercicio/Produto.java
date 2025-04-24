package A03_ARA0075_POO_NA.aula10_exercicio;

public class Produto extends ItemEstoque implements OperacaoEstoque {
    public Produto(int id, String nome, int quantidade, double valor) {
        super(id, nome, quantidade, valor);
    }

    public synchronized void adicionarEstoque(int qtd) {
        setQuantidade(getQuantidade() + qtd);
        System.out.println("Adicionando " + qtd + " unidades ao produto: " + getNome());
    }

    public synchronized void retirarEstoque(int qtd) {
        if (getQuantidade() >= qtd) {
            setQuantidade(getQuantidade() - qtd);
            System.out.println("Retirando " + qtd + " unidades do produto: " + getNome());
        } else {
            throw new IllegalArgumentException("Quantidade insuficiente em estoque para o produto: " + getNome());
        }
    }

    @Override
    public void realizarOperacao() {
        System.out.println("Operação genérica realizada no produto: " + getNome());
    }

    @Override
    public void exibirInformacoes() {
        System.out.println("Produto: " + getNome() + " - Quantidade: " + getQuantidade() + " - Valor: " + getValor());
    }
}
