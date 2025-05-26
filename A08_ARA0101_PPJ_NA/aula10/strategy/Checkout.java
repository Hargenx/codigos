package A08_ARA0075_PPS_NA.aula10.strategy;

public class Checkout {
    private FreteStrategy frete;

    public void setFrete(FreteStrategy frete) {
        this.frete = frete;
    }

    public double calcularFrete(double peso) {
        return frete.calcular(peso);
    }
}