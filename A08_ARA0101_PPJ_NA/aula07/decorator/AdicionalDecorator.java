package A08_ARA0075_PPS_NA.aula07.decorator;

public abstract class AdicionalDecorator implements Bebida {
    protected Bebida bebida;

    public AdicionalDecorator(Bebida bebida) {
        this.bebida = bebida;
    }
}