package A08_ARA0075_PPS_NA.aula07.bridge;

public class MensagemSimples extends Mensagem {
    public MensagemSimples(CanalEnvio canal) {
        super(canal);
    }

    public void enviarMensagem(String texto) {
        canal.enviar("Mensagem simples: " + texto);
    }
}
