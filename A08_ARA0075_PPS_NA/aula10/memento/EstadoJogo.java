package A08_ARA0075_PPS_NA.aula10.memento;
public class EstadoJogo {
    private final String posicao;

    public EstadoJogo(String posicao) {
        this.posicao = posicao;
    }

    public String getPosicao() {
        return posicao;
    }
}