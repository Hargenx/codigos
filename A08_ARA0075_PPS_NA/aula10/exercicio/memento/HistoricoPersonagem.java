package A08_ARA0075_PPS_NA.aula10.exercicio.memento;

import java.util.Stack;

public class HistoricoPersonagem {
    private Stack<EstadoPersonagem> historico = new Stack<>();

    public void salvar(EstadoPersonagem estado) {
        historico.push(estado);
    }

    public EstadoPersonagem restaurar() {
        if (!historico.isEmpty()) {
            return historico.pop();
        }
        return null;
    }
}
