package A08_ARA0075_PPS_NA.aula09.command;

public class AcenderLuz implements Comando {
    public void executar() {
        System.out.println("💡 Luz acesa");
    }

    public void desfazer() {
        System.out.println("💡 Luz apagada");
    }
}