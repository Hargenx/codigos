package A02_ARA0101_PPJ_CG.padrao_grasp.model;

import java.util.ArrayList;
import java.util.List;

// Especialista + Criador
public class Pedido {
    private List<ItemPedido> itens = new ArrayList<>();

    public void adicionarItem(Produto produto, int qtde) {
        itens.add(new ItemPedido(produto, qtde)); // Criador
    }

    public double calcularTotal() { // Especialista
        return itens.stream().mapToDouble(ItemPedido::subtotal).sum();
    }
}