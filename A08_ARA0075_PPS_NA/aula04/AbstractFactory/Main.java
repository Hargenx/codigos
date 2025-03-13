package A08_ARA0075_PPS_NA.aula04.AbstractFactory;

public class Main {
    public static void main(String[] args) {
        // Suponha que a plataforma seja Windows.
        GUIFactory factory = new WindowsFactory();

        Button button = factory.createButton();
        Menu menu = factory.createMenu();

        button.paint(); // Saída: "Renderizando um botão no estilo Windows."
        menu.paint(); // Saída: "Renderizando um menu no estilo Windows."

        // Caso a plataforma seja macOS, basta trocar a fábrica:
        factory = new MacFactory();

        button = factory.createButton();
        menu = factory.createMenu();

        button.paint(); // Saída: "Renderizando um botão no estilo macOS."
        menu.paint(); // Saída: "Renderizando um menu no estilo macOS."
    }
}
