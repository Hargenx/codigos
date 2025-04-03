package A08_ARA0075_PPS_NA.aula07.composite;

import java.util.ArrayList;
import java.util.List;

public class ProdutoComposto implements Produto {
    private String nome;
    private List<Produto> itens = new ArrayList<>();

    public ProdutoComposto(String nome) {
        this.nome = nome;
    }

    public void adicionar(Produto p) {
        itens.add(p);
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return itens.stream().mapToDouble(Produto::getPreco).sum();
    }
}
