package A02_ARA0101_PPJ_CG.aula02.FactoryMethod.exemplo01;

import java.util.ArrayList;
import java.util.List;

public abstract class Pedido {
    protected List<PedidoItem> itens = new ArrayList<>();

    // Método-fábrica abstrato
    protected abstract PedidoItem criarItem(Produto produto, int quantidade);

    public void adicionarItem(Produto produto, int quantidade) {
        PedidoItem item = criarItem(produto, quantidade);
        itens.add(item);
    }

    public List<PedidoItem> getItens() {
        return itens;
    }

    // Apenas para demonstrar
    public double calcularTotal() {
        double total = 0.0;
        for (PedidoItem item : itens) {
            total += item.getPreco();
        }
        return total;
    }
}
