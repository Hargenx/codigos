package A08_ARA0075_PPS_NA.aula07.bridge;

public abstract class Mensagem {
    protected CanalEnvio canal;

    public Mensagem(CanalEnvio canal) {
        this.canal = canal;
    }

    public abstract void enviarMensagem(String texto);
}