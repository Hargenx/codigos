package exemplo01;

public class Main {
    public static void main(String[] args) {
        // Criando um pedido para loja física
        Pedido pedidoLoja = new PedidoLojaFisica();
        pedidoLoja.adicionarItem(new Produto("Caderno", 20.0), 2);
        pedidoLoja.adicionarItem(new Produto("Caneta", 2.0), 5);

        System.out.println("Itens no Pedido da Loja Física:");
        for (PedidoItem item : pedidoLoja.getItens()) {
            System.out.println("- " + item.getProduto().getNome() +
                    " x" + item.getQuantidade() +
                    " => R$ " + item.getPreco());
        }
        System.out.println("Total: R$ " + pedidoLoja.calcularTotal());

        // Criando um pedido online
        Pedido pedidoOnline = new PedidoOnline();
        pedidoOnline.adicionarItem(new Produto("Livro", 50.0), 1);
        pedidoOnline.adicionarItem(new Produto("Mouse", 80.0), 1);

        System.out.println("\nItens no Pedido Online:");
        for (PedidoItem item : pedidoOnline.getItens()) {
            System.out.println("- " + item.getProduto().getNome() +
                    " x" + item.getQuantidade() +
                    " => R$ " + item.getPreco());
        }
        System.out.println("Total: R$ " + pedidoOnline.calcularTotal());
    }
}
