package A08_ARA0075_PPS_NA.aula04.AbstractFactory;

public class MacButton implements Button {
    @Override
    public void paint() {
        System.out.println("Renderizando um botão no estilo macOS.");
    }
}