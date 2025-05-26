package A08_ARA0075_PPS_NA.aula10.strategy;

public class Transportadora implements FreteStrategy {
    public double calcular(double peso) {
        return 30 + peso * 1.2;
    }
}