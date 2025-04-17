package A08_ARA0075_PPS_NA.aula09.command;

public class MainCommand {
    public static void main(String[] args) {
        ControleRemoto controle = new ControleRemoto();
        controle.executarComando(new AcenderLuz());
        controle.executarComando(new LigarTV());

        System.out.println("↩ Desfazendo última ação:");
        controle.desfazerUltimo();
    }
}
