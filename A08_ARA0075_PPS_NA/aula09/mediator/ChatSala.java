package A08_ARA0075_PPS_NA.aula09.mediator;

public interface ChatSala {
    void enviar(String mensagem, Usuario remetente);

    void registrarUsuario(Usuario usuario);
}
