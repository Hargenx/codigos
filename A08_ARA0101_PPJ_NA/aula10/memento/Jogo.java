package A08_ARA0075_PPS_NA.aula10.memento;
public class Jogo {
    private String posicao = "A1";

    public void moverPara(String novaPosicao) {
        System.out.println("Movendo para " + novaPosicao);
        posicao = novaPosicao;
    }

    public EstadoJogo salvar() {
        return new EstadoJogo(posicao);
    }

    public void restaurar(EstadoJogo estado) {
        this.posicao = estado.getPosicao();
        System.out.println("Desfeito! Voltou para " + posicao);
    }

    public String getPosicao() {
        return posicao;
    }
}
