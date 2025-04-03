package A08_ARA0075_PPS_NA.aula07.decorator;

public class Leite extends AdicionalDecorator {
    public Leite(Bebida bebida) {
        super(bebida);
    }

    public String getDescricao() {
        return bebida.getDescricao() + ", com leite";
    }

    public double getPreco() {
        return bebida.getPreco() + 1.0;
    }
}
