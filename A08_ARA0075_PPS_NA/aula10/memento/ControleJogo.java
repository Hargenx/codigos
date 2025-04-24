package A08_ARA0075_PPS_NA.aula10.memento;
import java.util.Stack;

public class ControleJogo {
    private Stack<EstadoJogo> historico = new Stack<>();

    public void salvar(EstadoJogo estado) {
        historico.push(estado);
    }

    public EstadoJogo desfazer() {
        if (!historico.isEmpty()) {
            return historico.pop();
        }
        return null;
    }
}
