package A08_ARA0075_PPS_NA.aula04.AbstractFactory;

public class MacMenu implements Menu {
    @Override
    public void paint() {
        System.out.println("Renderizando um menu no estilo macOS.");
    }
}