package A08_ARA0075_PPS_NA.aula10.exercicio.memento;

public class EstadoPersonagem {
    private final int vida;
    private final int energia;

    public EstadoPersonagem(int vida, int energia) {
        this.vida = vida;
        this.energia = energia;
    }

    public int getVida() {
        return vida;
    }

    public int getEnergia() {
        return energia;
    }
}
