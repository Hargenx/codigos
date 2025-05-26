package A02_ARA0101_PPJ_CG.aula12.state;

public class Main {
    public static void main(String[] args) {
        Pedido pedido = new Pedido();
        pedido.avancar(); // Avança para Processado
        //pedido.cancelar();
        pedido.avancar(); // Avança para Entregue
        pedido.cancelar(); // Não pode cancelar, já entregue
    }
}