package A08_ARA0075_PPS_NA.aula08.Flyweight;

public class TemplateHTML implements EmailTemplate {
    private String layout;

    public TemplateHTML(String layout) {
        this.layout = layout;
    }

    public void render(String conteudo) {
        System.out.println("Layout: " + layout);
        System.out.println("Conteúdo personalizado: " + conteudo);
        System.out.println("Email enviado!\n");
    }
}
