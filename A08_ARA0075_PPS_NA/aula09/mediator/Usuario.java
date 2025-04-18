package A08_ARA0075_PPS_NA.aula09.mediator;

public class Usuario {
    private String nome;
    private ChatSala sala;

    public Usuario(String nome, ChatSala sala) {
        this.nome = nome;
        this.sala = sala;
        sala.registrarUsuario(this);
    }

    public void enviar(String mensagem) {
        sala.enviar(mensagem, this);
    }

    public void receber(String mensagem) {
        System.out.println(nome + " recebeu: " + mensagem);
    }
}
