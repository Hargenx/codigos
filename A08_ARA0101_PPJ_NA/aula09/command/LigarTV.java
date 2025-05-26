package A08_ARA0075_PPS_NA.aula09.command;

public class LigarTV implements Comando {
    public void executar() {
        System.out.println("📺 TV ligada");
    }

    public void desfazer() {
        System.out.println("📺 TV desligada");
    }
}