package A08_ARA0075_PPS_NA.aula07.composite;

public class Main {
    public static void main(String[] args) {
        Produto mouse = new ProdutoSimples("Mouse", 50);
        Produto teclado = new ProdutoSimples("Teclado", 100);
        ProdutoComposto kit = new ProdutoComposto("Kit Escritório");
        kit.adicionar(mouse);
        kit.adicionar(teclado);
        System.out.println(kit.getNome() + " custa R$" + kit.getPreco());
        System.out.println(mouse.getNome() + " custa R$" + mouse.getPreco());
        System.out.println(teclado.getNome() + " custa R$" + teclado.getPreco());
    }
}
