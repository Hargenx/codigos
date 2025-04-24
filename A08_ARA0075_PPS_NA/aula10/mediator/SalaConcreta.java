package A08_ARA0075_PPS_NA.aula10.mediator;

import java.util.ArrayList;
import java.util.List;

public class SalaConcreta implements ChatSala {
    private List<Usuario> usuarios = new ArrayList<>();

    public void registrarUsuario(Usuario usuario) {
        usuarios.add(usuario);
    }

    public void enviar(String mensagem, Usuario remetente) {
        for (Usuario u : usuarios) {
            if (u != remetente) {
                u.receber(mensagem);
            }
        }
    }
}
