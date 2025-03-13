package A08_ARA0075_PPS_NA.aula04.AbstractFactory;

public class WindowsMenu implements Menu {
    @Override
    public void paint() {
        System.out.println("Renderizando um menu no estilo Windows.");
    }
}