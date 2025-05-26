package A08_ARA0075_PPS_NA.aula08.Flyweight;

public class Main {
    public static void main(String[] args) {
        TemplateFactory factory = new TemplateFactory();

        EmailTemplate templateBoasVindas = factory.getTemplate("Boas-vindas");
        EmailTemplate templatePromocao = factory.getTemplate("Promoção");

        templateBoasVindas.render("Olá João, bem-vindo à nossa plataforma!");
        templateBoasVindas.render("Olá Maria, sua conta foi criada com sucesso!");

        templatePromocao.render("João, confira nossas promoções!");
    }
}
