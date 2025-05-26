package A08_ARA0075_PPS_NA.aula07.decorator;

public class Chocolate extends AdicionalDecorator {
    public Chocolate(Bebida bebida) {
        super(bebida);
    }

    public String getDescricao() {
        return bebida.getDescricao() + ", com chocolate";
    }

    public double getPreco() {
        return bebida.getPreco() + 1.5;
    }
}
