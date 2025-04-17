package A08_ARA0075_PPS_NA.aula09.command;

import java.util.Stack;

public class ControleRemoto {
    private Stack<Comando> historico = new Stack<>();

    public void executarComando(Comando comando) {
        comando.executar();
        historico.push(comando);
    }

    public void desfazerUltimo() {
        if (!historico.isEmpty()) {
            historico.pop().desfazer();
        }
    }
}
