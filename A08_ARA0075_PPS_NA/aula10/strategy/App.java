package A08_ARA0075_PPS_NA.aula10.strategy;

public class App {
    public static void main(String[] args) {
        Checkout pedido = new Checkout();

        pedido.setFrete(new Sedex());
        System.out.println("Sedex: " + pedido.calcularFrete(5));

        pedido.setFrete(new PAC());
        System.out.println("PAC: " + pedido.calcularFrete(5));

        pedido.setFrete(new Transportadora());
        System.out.println("Transportadora: " + pedido.calcularFrete(5));
    }
}
