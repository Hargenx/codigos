package A08_ARA0075_PPS_NA.aula07.bridge;

// Teste
public class Main {
    public static void main(String[] args) {
        Mensagem msg = new MensagemSimples(new Email());
        msg.enviarMensagem("Relatório enviado.");
    }
}
