package A08_ARA0075_PPS_NA.aula10.mediator;

public class MainMediator {
    public static void main(String[] args) {
        ChatSala sala = new SalaConcreta();

        Usuario rapha = new Usuario("Raphael", sala);
        Usuario carol = new Usuario("Caroline", sala);
        Usuario sara = new Usuario("Sara", sala);

        rapha.enviar("Olá, pessoal!");
        carol.enviar("Oi, Raphael, oi Sara!");
        sara.enviar("Oi, Raphael e Caroline!");
    }
}
