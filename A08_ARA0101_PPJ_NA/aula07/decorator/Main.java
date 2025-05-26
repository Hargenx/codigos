package A08_ARA0075_PPS_NA.aula07.decorator;

public class Main {
    public static void main(String[] args) {
        Bebida pedido = new Leite(new Chocolate(new Cafe()));
        System.out.println(pedido.getDescricao());
        System.out.println("Total: R$" + pedido.getPreco());
    }
}
